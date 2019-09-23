# wcf
Workers Compensation Fund Project

This is the django api for the requested project.  The project uses a REST API with CORS headers enabled so a Vue.js UI
can connect.  If I had more time, I would build the UI end utilizing Vue.js, BootstrapVue.js, and Vuelidate
to validate the form data.  Development is taking place on the 'devel' branch.  The project when running is 
available at 'http://127.0.0.1:8000/api/';  In addition, the admin interface is enabled and available at 
'http://127.0.0.1:8000/admin'

Django is setup to use an sqlite database for development purposes.  All of the Django projects I have built in my
resume are running with MySQL databases.

In order to run the project, please insure your virtual environment contains the libraries in requirements.txt and
in a terminal run 'python manage.py runserver 127.0.0.1:8000'.

In order to utilize the admin section of Django, a superuser 
needs to be created by running 'python manage.py createsuperuser --username < username >'

Thank you for your consideration,

Darren Tanner
