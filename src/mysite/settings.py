"""Configure Setting"""
import os
from mysite.secrets import (
  EMAIL,
  DATABASE,
  KEY
)
from mysite.jet import MENU, THEMES

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = KEY
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  'localhost',
  '34.199.187.54',
  'www.ryusukelavalla.com',
  'ryusukelavalla.com'
]
# Application definition
INSTALLED_APPS = [
    'jet.dashboard', #Admin App
    'jet', #Admin App
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #3rd-Party Apps
    'analytical',
    'debug_toolbar',
    'djangobower',
    'djangoseo',
    'materializecssform',
    'sass_processor',
    'robots',
    #myApp
    'website',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

# Email Setup
EMAIL_HOST = EMAIL['host']
EMAIL_HOST_USER = EMAIL['user']
EMAIL_HOST_PASSWORD = EMAIL['password']
EMAIL_PORT = EMAIL['port']
EMAIL_USE_TLS = True

# WSGI
WSGI_APPLICATION = 'mysite.wsgi.application'

#Djnago Site
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE['name'],
        'USER': DATABASE['user'],
        'PASSWORD': DATABASE['password'],
        'HOST': DATABASE['host'],
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'sass_processor.finders.CssFinder',
)
#Bower Setup
BOWER_INSTALLED_APPS = (
    'components-font-awesome',
    'jquery',
    'parallax.js',
    'materialize',
    'scrollreveal',
    'typed.js'
)

#Sass Compression
SASS_PROCESSOR_ROOT = 'static'

#Debug Tool
INTERNAL_IPS = '127.0.0.1'

#Admin
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
JET_SIDE_MENU_COMPACT = True
JET_SIDE_MENU_CUSTOM_APPS = MENU
JET_CHANGE_FORM_SIBLING_LINKS = True
JET_THEMES = THEMES

#Google SEO
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-73569010-1'
GOOGLE_ANALYTICS_SITE_SPEED = True
