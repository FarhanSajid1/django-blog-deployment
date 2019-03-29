from .base import *
import os

'''Database parameters!'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('postgres', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASS', 'postgres_password'),
        'PORT': '5432',
        'HOST': 'postgres'
    }
}
