from .base import *
from decouple import config, Csv
import django_on_heroku

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())


#AWS S3 settings
#AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

#AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

#AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

#AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#ex: http://my-app-bucket.s3.amazonaws.com/static/

#AWS_DEFAULT_ACL = 'public-read'

#AWS_S3_OBJECT_PARAMETERS = {
#    'CacheControl': 'max-age=86400'
#}

#AWS_LOCATION = 'static'

#AWS_QUERYSTRING_AUTH = False

#AWS_HEADERS = {
#    'Access-Control-Allow-Origin': '*',
#}

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

#MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


#Heroku logging
DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}


#Heroku settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
