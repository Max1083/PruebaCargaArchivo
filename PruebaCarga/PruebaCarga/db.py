import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SQLITE ={
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
} 

POSTGRESSQL ={
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'APPS_STORE',
        'USER': 'postgres',
        'PASSWORD': 'Faleita10',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

MYSQL ={
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cargar',
        'USER': 'root',
        'PASSWORD': 'Faleita10',
        'HOST': 'localhost',
        'PORT': '3306',

    }


}