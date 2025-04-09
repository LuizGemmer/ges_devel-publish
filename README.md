# ges_django_todo_app
App developed in the class of Settings Management and Cloud Computing of the course software engenieering at Universidade do Vale do Taquari - Univates

## The App
The app setup 2 containers, one basic Postgresql and other with the Django App.
The app, for now, serves a simple table reading the contents of the todo table. That's it. No CRUD.
As of packages, uses guinicorn as a WSGI server for Django + the Django and psycopg packages.

## Architechture
The Dockerfile and compose.yml were adapted from https://www.docker.com/blog/how-to-dockerize-django-app/. Changed the CMD param of the Dockerfile to use the entrypoint.prod.sh script, so that the database migrations would run on container build.


## Execution
Clone this repo, cd into the folder with the files, setup a .env file based on .env_example.txt and run:

docker compose up --build