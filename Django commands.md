# Django commands

## Start Project

```shell
django-admin startproject project-name
cd project-name
```

## Start app

```shell
python manage.py startapp app-name
```

## Make migrations

```shell
python manage.py makemigrations
```

## Make database structure

```shell
python manage.py sqlmigrate app-name 0001
```

## Migrate

```shell
python manage.py migrate
```

## Run server

```shell
python manage.py runserver
```