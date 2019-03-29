from .base import *

DEBUG = True

SECRET_KEY =  'afoiajsfoija84284uijskflkamlfkmaskfjaofjoa'

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

ALLOWED_HOSTS = [
    '*'
]
# static/media urls and roots
MEDIA_ROOT = '/var/www/blog/media/'
STATIC_ROOT = '/var/www/blog/static/'
STATIC_URL = '/static/'




