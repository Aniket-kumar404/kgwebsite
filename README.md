# kgwebsite

This is an django rest api app which display registerd employee name and also provide option to add employee and then it saves to the database for getting more details about employee 
tap on gvie section that is provided beside the name in the table 

Quick start guide:
Installation:

    1. Install django:
    2. pip install django
    3. create virtual enviroment
`   4. python -m venv venv
    5. venv\Scripts\activate
    6. to get connected with data base install psycopg2
    7. pip install psycopg2
    8. then the following command in terminal
    9. python manage.py runserver
     
 
To connected with data u need to run following commands , in my case i am using postgresql
 
1. set up database config in setting.py
        
      
DATABASES = {
  'default': {
               
        'ENGINE': 'django.db.backends.postgresql',
        #name of the database should be declared below
        'NAME': 'employee',

        #User name of the database
        'USER':'',
        #password of the databasse
        'PASSWORD':'',
        #host =localhost
       'Host':'localhost',
       
    }
 }

2. python manage.py makemigrations 
3. afterwards it will create migrations in file in same direcory under migration folder like 0001_initial
4. python manage.py sqlmigrate employeeoform 0001
5. python migrate



