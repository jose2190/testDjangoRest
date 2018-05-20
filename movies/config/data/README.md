## Simple example of Django Rest Framework
This is a sample project using Django with REST calls, using django-rest-framework.
# Why Django?
>First of all django is by far one of the best frameworks on the market (sorry laravel and rails), second, has an excellent community that supports, improves and refines the tool (sometimes it breaks it down a bit, but in its large most improvement), and third is because it is Python!


## Why Django Rest framework?
>Well, to detail a little more the panorama, let's see this: To work with Django and rest at the same time there are 4 alternatives:
* Use Django Rest Framework (https://github.com/encode/django-rest-framework)
* Use Django TastiePie (https://github.com/django-tastypie/django-tastypie)
* Make it by hand through views and the json library
* Do not use REST

> **But to be fair the main reasons are:**
* Full compatibility with python 3 and Django 2.0 (almost) 
* Excellent Documentation (seriously, incredibly well documented, in the best django style)
* An extensive community
* Many tutorials
* Many issues resolved on github

# Live Demo
> Go to http://51.15.135.208:8080 


# Usage:

> **Local Development (Virtual Env):**
``` sh
sh install-dev.sh
```
This command will create a directory for the virtual environment, start python3 inside, install the dependencies of the project and run the migrations.

* *Please be sure to have python3 and pip installed in your computer.*


> **Local Development (Docker):**

```sh
docker-compose -f docker-compose.yml up 
```

This command will start docker with 2 containers, one for postgres and the other with django.
In the container that runs django it will start in development mode (```python manage.py runserver 0.0.0.0:8000```), first running the migrations and assigning the corresponding configuration to the database (see `config/infrastructure.py` for more information).

> **Production (Docker):**
```sh
docker-compose -f docker-compose.prod.yml up
```
This command will start docker with 2 containers, one for postgres and the other with django.
In the container that runs django it will start in production mode with gunicorn, first running the migrations and assigning the corresponding configuration to the database (see `config/infrastructure.py` for more information).

# Environment Variables
To customize a database configuration path you can assign an environment variable with the name `DJANGODBCONFIG` and in its value a path to a json file with the corresponding information following the standardized format of django to assign to the variable DATABASE in `settings.py`
For example:

```json
{
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "movies",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "localhost",
        "PORT": 5432
    }
}
```
# API Rest Endpoints 
This project has 3 main endpoints
  - `/api/person`
  - `/api/movie`
  - `/docs/`
 
>**In the endpoint / docs / you can find the documentation on how to interact with the API, as well as a simulator to make requests.**