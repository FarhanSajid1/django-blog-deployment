from .base import *

DEBUG = False

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
    '127.0.0.1:8990',
    '127.0.0.1'
]
'''Adding s3 Support'''
INSTALLED_APPS +=['storages']

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'http://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# S3 CONFIGURATIONS
AWS_STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'

AWS_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'
