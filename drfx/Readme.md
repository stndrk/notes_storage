# notes_storage

A framework for launching new Django Rest Framework projects quickly. Comes with a custom user model, login/logout/signup, social authentication via django-allauth, and more.

## Features

- Django 3.1, Django REST Framework 3.12, and Python 3.8
- Custom user model
- Token-based auth
- Signup/login/logout
- [django-allauth](https://github.com/pennersr/django-allauth) for social auth
- [Pipenv](https://github.com/pypa/pipenv) for virtualenvs

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/wsvincent/notes_storage.git
$ cd notes_storage
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration for our custom user models in users and build the database.

```
(notes_storage) $ python manage.py makemigrations users
(notes_storage) $ python manage.py migrate
(notes_storage) $ python manage.py createsuperuser
(notes_storage) $ python manage.py runserver
```

4.  Endpoints

Login with your superuser account. Then navigate to all users. Logout. Sign up for a new account and repeat the login, users, logout flow.

- login - http://127.0.0.1:8000/api/v1/rest-auth/login/
- all users - http://127.0.0.1:8000/api/v1/users
- logout - http://127.0.0.1:8000/api/v1/rest-auth/logout/
- signup - http://127.0.0.1:8000/api/v1/rest-auth/registration/

---

Want to learn more about Django REST Framework? I've written an entire book that takes a project-based approach to building web APIs with Django. The first 2 chapters are available for free online at [https://djangoforapis.com/](https://djangoforapis.com/).

[![Django for APIs](https://learndjango.com/static/images/books/dfa_cover_31.jpg)](https://djangoforapis.com)
