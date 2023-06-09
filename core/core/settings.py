from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-njh8fj^py b+=b6^9_50xa9$z*20ul1b+2*)mv%ga)j!gskrya2@*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition


SHARED_APPS = (
    'django_tenants',  # mandatory
    'client',  # you must list the app where your tenant model resides in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notifications',
    'rest_framework',
    'accounts',
    'rest_framework_simplejwt',
    'homepage'

)

TENANT_APPS = (
    # your tenant-specific apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notifications',
    'rest_framework',
    'accounts',
    'rest_framework_simplejwt',
    'homepage'
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]
TENANT_MODEL = "client.Client"  # app.Model
TENANT_DOMAIN_MODEL = "client.Domain"  # app.Model

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
PUBLIC_SCHEMA_URLCONF = 'core.urls_public'
AUTH_USER_MODEL = 'accounts.Account'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {

        # 'ENGINE': 'django_tenants.postgresql_backend',
        # 'NAME': 'postgres',
        # 'USER': 'master',
        # 'PASSWORD': '*cAzLT398wD5',
        # 'HOST': 'alcor-dev-high5-cloud-postgres-rds.cjlu8mvrnu5r.ap-south-1.rds.amazonaws.com',
        # 'PORT': '5432',

        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'test1',
        'USER': 'postgres',
        'PASSWORD': 'Abhay786',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True
