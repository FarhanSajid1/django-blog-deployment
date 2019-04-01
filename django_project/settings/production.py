from .base import *

DEBUG = False

SECRET_KEY = 'afoiajsfoija84284uijskflkamlfkmaskfjaofjoa'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE', ),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'PORT': os.environ.get('PGPORT'),
        'HOST': os.environ.get('PGHOST')
    }
}

ALLOWED_HOSTS = [
    'http://deployment-env.jt2r2hfekg.us-east-2.elasticbeanstalk.com/',
    '.compute-1.amazonaws.com',
    '.elasticbeanstalk.com',
    "localhost"
]
# static/media urls and roots for production
MEDIA_ROOT = '/var/www/blog/media/'

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/blog/static/'


# USE_S3 = True
USE_S3 = os.environ.get('USE_S3')
if USE_S3:
    # aws settings
    INSTALLED_APPS += ['storages']
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'us-east-2'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    SENDFILE_BACKEND = 'sendfile.backends.simple'
else:
    MEDIA_ROOT = '/var/www/blog/media/'
    MEDIA_URL = '/media/'




