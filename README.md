# ges_django_todo_app
App developed in the class of settings management of the course software engenieering at Universidade do Vale do Taquari - Univates

## Start up
Clone this repo, cd into the folder with the files and run:
docker compose up --build
ctrl+c
docker run django-web python manage.py migrate
docker compose up --build