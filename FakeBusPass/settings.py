"""
Django settings for FakeBusPass project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^n8ltyx-*l5o05p8a(g**eymv*15+yh1ala63h6j5sv@gqdrjv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminapp',
    'conductorapp',
    'mainapp',
    'userapp',
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

ROOT_URLCONF = 'FakeBusPass.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'assets/templates')],
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

WSGI_APPLICATION = 'FakeBusPass.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fakebuspassdetection',
        'HOST': '127.0.0.10',
        'USER': 'root',
        'PASSWORD': '',
        'PORT':'3306',
        'OPTION':{
            'init_command':"SET sql-mode='STRICT-TRAINS_TABLES" 
            }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'assets/static'),]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
MEDIA_URL='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from .emailsetting import SET_EMAIL_USE_TLS, SET_EMAIL_HOST, SET_EMAIL_HOST_USER, \
    SET_EMAIL_HOST_PASSWORD, SET_EMAIL_PORT, SET_EMAIL_BACKEND, SET_DEFAULT_FROM_EMAIL

EMAIL_USE_TLS = SET_EMAIL_USE_TLS
EMAIL_HOST = SET_EMAIL_HOST
EMAIL_HOST_USER = SET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SET_EMAIL_HOST_PASSWORD
EMAIL_PORT = SET_EMAIL_PORT
EMAIL_BACKEND = SET_EMAIL_BACKEND
DEFAULT_FROM_EMAIL = SET_DEFAULT_FROM_EMAIL
