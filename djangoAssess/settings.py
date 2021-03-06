"""
Django settings for djangoAssess project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from django.contrib.messages import constants as messages
import os
import dj_database_url

from pathlib import Path
import pymysql  # noqa: 402
pymysql.install_as_MySQLdb()


MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a3*5llfol*z6b^jk2bb)!5)uoa6@z&87s*1u-z%pp6b(x@8x-d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1", "*"]
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dashboard",
    "dashboard.templatetags",
    "corsheaders",
    'multiselectfield',
    'jsignature',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
 'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]
CORS_ALLOWED_ORIGINS = [
    "https://domain.com",
    "https://api.domain.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
    "https://72a5-122-173-29-11.ngrok.io",
]
CSRF_TRUSTED_ORIGINS = ["https://e221-122-173-29-11.ngrok.io"]

ROOT_URLCONF = "djangoAssess.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangoAssess.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# if os.getenv('GAE_APPLICATION', None):
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.mysql",
#             "HOST": '/cloudsql/gentle-habitat-344411:us-central1:shaping-instance',
#             "USER": 'shapinguser',
#             "PASSWORD": 'qmXs)Ftr`/P}<G2B',
#             "NAME": "shapingdb"
#         }
#     }
# else:


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# DATABASES['default']['HOST'] = '/cloudsql/gentle-habitat-344411:us-central1:shaping-instance'
# if os.getenv('GAE_INSTANCE'):
#     pass
# else:
#     DATABASES['default']['HOST'] = '127.0.0.1'
#     DATABASES['default']['PORT'] = '3306'
#     DATABASES['default']['USER'] = 'shapinguser'
#     DATABASES['default']['PASSWORD'] = 'qmXs)Ftr`/P}<G2B'
#     DATABASES['default']['NAME'] = 'shapingdb'
#     DATABASES['default']['PORT'] = '3306'


if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            "HOST": '/cloudsql/gentle-habitat-344411:us-central1:shaping-instance',
            "USER": 'shapinguser',
            "PASSWORD": 'qmXs)Ftr`/P}<G2B',
            "NAME": "shapingdb",
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    }
    
    WHITENOISE_USE_FINDERS = True

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = "Y-m-d"

TIME_INPUT_FORMATS = ("%H:%M %p",)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

AUTH_USER_MODEL = "dashboard.User"

# Add these new lines
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
ROOT_URLCONF = "djangoAssess.urls"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
DEBUG = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "vishalmehta@snakescript.com"
EMAIL_HOST_PASSWORD = "asgcpdcxyjztytpt"
EMAIL_PORT = 587

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE =  'django.contrib.staticfiles.storage.StaticFilesStorage'