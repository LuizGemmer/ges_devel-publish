from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .forms import TaskForm, TaskUpdateForm
from .models import Tasks

class TaskFormTests(TestCase):

    def setUp(self):
        self.valid_data = {
            'descricao': 'Comprar materiais',
            'data_prevista': (timezone.now() + timedelta(days=1)).date()
        }

    def test_valid_task_form(self):
        form = TaskForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_missing_required_fields(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('descricao', form.errors)
        self.assertIn('data_prevista', form.errors)

    def test_form_fields_presence(self):
        form = TaskForm()
        self.assertSetEqual(set(form.fields.keys()), {'descricao', 'data_prevista'})

    def test_widgets_applied_correctly(self):
        form = TaskForm()
        self.assertIn('class="form-control"', str(form['descricao']))
        self.assertIn('type="date"', str(form['data_prevista']))

    def test_invalid_date_format(self):
        data = self.valid_data.copy()
        data['data_prevista'] = 'invalid-date'
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('data_prevista', form.errors)


class TaskUpdateFormTests(TestCase):

    def setUp(self):
        self.valid_data = {
            'descricao': 'Atualizar sistema',
            'data_prevista': timezone.now().date(),
            'situacao': 'concluida',
            'data_conclusao': timezone.now().date()
        }

    def test_valid_update_form(self):
        form = TaskUpdateForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_required_fields_validation(self):
        form = TaskUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('descricao', form.errors)
        self.assertIn('data_prevista', form.errors)

    def test_invalid_choice_in_situacao(self):
        bad_data = self.valid_data.copy()
        bad_data['situacao'] = 'inexistente'
        form = TaskUpdateForm(data=bad_data)
        self.assertFalse(form.is_valid())
        self.assertIn('situacao', form.errors)

    def test_invalid_date_in_data_conclusao(self):
        bad_data = self.valid_data.copy()
        bad_data['data_conclusao'] = 'not-a-date'
        form = TaskUpdateForm(data=bad_data)
        self.assertFalse(form.is_valid())
        self.assertIn('data_conclusao', form.errors)

    def test_data_conclusao_before_data_prevista(self):
        # Optional: depends if your model/form does this logic
        # Here we just set up the idea in case you add clean() logic
        data = self.valid_data.copy()
        data['data_conclusao'] = timezone.now().date() - timedelta(days=3)
        form = TaskUpdateForm(data=data)
        # This will pass unless you explicitly add logic to check this
        self.assertTrue(form.is_valid())

    def test_form_fields_presence(self):
        form = TaskUpdateForm()
        self.assertSetEqual(
            set(form.fields.keys()),
            {'descricao', 'data_prevista', 'situacao', 'data_conclusao'}
        )

    def test_widgets_applied_correctly(self):
        form = TaskUpdateForm()
        self.assertIn('class="form-control"', str(form['descricao']))
        self.assertIn('type="date"', str(form['data_conclusao']))
        self.assertIn('class="form-control"', str(form['situacao']))


class TasksModelTest(TestCase):

    def setUp(self):
        self.task = Tasks.objects.create(
            descricao="Testar sistema",
            data_prevista=timezone.now().date() + timedelta(days=1)
        )

    def test_task_creation(self):
        self.assertIsInstance(self.task, Tasks)
        self.assertIsNotNone(self.task.id)
        self.assertEqual(self.task.descricao, "Testar sistema")
        self.assertEqual(self.task.situacao, "pendente")
        self.assertIsNone(self.task.data_conclusao)

    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Testar sistema")

    def test_default_situacao(self):
        self.assertEqual(self.task.situacao, "pendente")

    def test_update_task(self):
        self.task.descricao = "Nova descrição"
        self.task.situacao = "em andamento"
        self.task.save()
        updated = Tasks.objects.get(id=self.task.id)
        self.assertEqual(updated.descricao, "Nova descrição")
        self.assertEqual(updated.situacao, "em andamento")

    def test_data_conclusao_optional(self):
        self.task.data_conclusao = timezone.now().date()
        self.task.save()
        self.assertIsNotNone(self.task.data_conclusao)

    def test_invalid_situacao_choice(self):
        # This bypasses form validation, so model allows it unless validated manually
        self.task.situacao = "invalido"
        with self.assertRaises(ValueError):
            self.task.full_clean()  # This triggers model validation

    def test_created_updated_timestamps(self):
        created_at = self.task.created_at
        updated_at = self.task.updated_at
        self.task.descricao = "Alterada"
        self.task.save()
        self.task.refresh_from_db()
        self.assertEqual(created_at, self.task.created_at)
        self.assertNotEqual(updated_at, self.task.updated_at)
