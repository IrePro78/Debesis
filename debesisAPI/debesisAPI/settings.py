import os

import django.utils.log
import environ
from pathlib import Path
import logging.config

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY', default='kluczyk')
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',
    'emails',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'debesisAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'debesisAPI.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('SQL_DATABASE'),
        'USER': env('SQL_USER'),
        'PASSWORD': env('SQL_PASSWORD'),
        'HOST': env('SQL_HOST'),
        'PORT': env('SQL_PORT'),
    }
}

# Celery Configuration Options
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = BASE_DIR / 'attachments/'
MEDIA_URL = '/attachments/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CELERY_HIJACK_ROOT_LOGGER = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            '()':'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standards': {
            'format': '%(levelname)s %(message)s',
            'datefmt': '%y %b %d, %H:%M:%S',
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/logs/email.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 3,
            'formatter': 'standard'
        },
        'debug_logfile': {
            'level': 'DEBUG',
            'filters': None,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/logs/debug_log.log',
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
    },
        'default_logger': {
                'level': 'WARNING',
                'filters': None,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/logs/default.log',
                'maxBytes': 1024*1024*5,
                'backupCount': 2,
                'formatter': 'standard'
        },
        'celery_log': {
                'level': 'DEBUG',
                'filters': None,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/logs/default.log',
                'maxBytes': 1024*1024*5,
                'backupCount': 2,
                'formatter': 'standard'
        },
        'celery_task_logger': {
                'level': 'DEBUG',
                'filters': None,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/logs/celery_tasks.log',
                'maxBytes': 1024*1024*5,
                'backupCount': 2,
                'formatter': 'standard'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default_logger'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,

        },
        'feedmanager': {
            'handlers': ['logfile', 'debug_logfile'],
            'level': 'DEBUG',
            'propagate': True,

        },
        'recipemanager': {
            'handlers': ['logfile', 'debug_logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'menumanager': {
            'handlers': ['logfile', 'debug_logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'celery.task': {
            'handlers': ['celery_task_logger'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'celery': {
            'handlers': ['cellery_logger'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
