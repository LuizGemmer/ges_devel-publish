from django.contrib import admin

from .models import Tasks, Test # , Category

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Test)
#admin.site.register(Category)

