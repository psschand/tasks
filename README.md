# Task Browser Demo

#Steps followed
started by creating our django project, by using the command below:

$django-admin.py startproject tasks

create a django app that holds the model and admin stuff, with the command below:

$manage.py startapp browser

updated settings with browser app

created model which deals with our database for the required tasks

created migration using the command line with the command below:

$manage.py makemigrations

then the command below to migrate the migrations

$manage.py migrate

create the templates folder, you can go ahead and create an “index.html”  and "details .html"
set up the api logic in views and route to frontend task id hyperlink by setting up  url and  updated the admin.py file in the browser app directory and created Tests.
added some styling for the table.

$ python manage.py runserver



## Installation for windows
```sh

$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
$ python tasks/manage.py runserver
```

## Installation for MAC
```sh

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python tasks/manage.py runserver
```

## Browser app

* ```tasks/browser``` folder contains the main Task Browser app

## Structure

* ```/tasks/browser/templates/browser/index.html``` is the main index file of the app
* ```/tasks/browser/templates/browser/detail.html``` is the the page which display the task in more detail
* ```/tasks/browser/models.py``` contains the ```Task``` model with status, duration and parent functions
* ```/tasks/browser/views.py``` contains ```index```, ```detail``` to render index.html and detail.html page
* ```/tasks/browser/views.py``` contains ```task_list```, ```task_detail```, ```task_detail``` to render ```/api/```, ```/api/1/```, ```/taskbrowser/interface/``` to create REST API
* ```/tasks/browser/tests.py``` to run tests
* ```/tasks/browser/admin.py``` to register Task module in Admin panel
