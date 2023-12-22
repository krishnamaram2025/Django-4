# Title
Django application to perform CRUD operations

# Technologies used
Frontend:  HTML

Backend: Django

Database: SQL


# Pre-Requisites
```
pip3 install Django
django-admin startproject webapp
python manage.py startapp portfolio
```

# Execution Flow
* Clone the project:
```
 git clone https://github.com/krishnamaram2025/CSP.git
```

* Install required packages:
```
 pip3 install -r requirements.txt
```

* Make migrations to database:
```
 python manage.py makemigrations
 python manage.py migrate
```
* Get admin access:
```
 python manage.py createsuperuser (enter username, email, password)
```

* Run server:
```
 python manage.py runserver => to run local
gunicorn main.wsgi --bind 0.0.0.0:8000 => to run on remore machine
```

* Testing
http://127.0.0.1:8000
http://127.0.0.1:8000/admin



# References
https://github.com/Jebaseelanravi/Portfolio-website-using-django

https://github.com/FahadulShadhin/crudapp.git

https://github.com/coluck/django-directory-template


