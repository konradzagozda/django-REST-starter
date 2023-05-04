import logging
import os
from pathlib import Path

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)

env = os.environ

try:
    loaded = env['LOADED']
except KeyError:
    raise ImproperlyConfigured('Environment file is not loaded')

# BEGIN DJANGO
DEBUG = env["DJANGO_DEBUG"]
SECRET_KEY = env["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = ["*"]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "drf_spectacular",
    "django_celery_results",
    "django_celery_beat",
]

LOCAL_APPS = ["common", "todo"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env["DB_NAME"],
        "USER": env["DB_USER"],
        "PASSWORD": env["DB_PASSWORD"],
        "HOST": env["DB_HOST"],
        "PORT": 5432,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env["EMAIL_HOST"]
EMAIL_PORT = env["EMAIL_PORT"]
REDIS_URL = "redis://" + env["REDIS_USERNAME"] + ":" + env["REDIS_PASSWORD"] + \
            "@" + env["REDIS_HOST"] + ":" + env["REDIS_PORT"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL + "/" + env["REDIS_CACHE_DB"],
    }
}

# END DJANGO

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS":
    "drf_spectacular.openapi.AutoSchema",
}

SITE_ID = 1  # https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional

SPECTACULAR_SETTINGS = {  # drf-spectacular
    "TITLE": "Todo API",
    "DESCRIPTION": "Starter project",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# ALLAUTH
ACCOUNT_EMAIL_VERIFICATION = env["ACCOUNT_EMAIL_VERIFICATION"]

CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 min task limit
CELERY_CACHE_BACKEND = "django-cache"

CELERY_BROKER_URL = ("amqp://" + env["RABBITMQ_USER"] + ":" +
                     env['RABBITMQ_PASSWORD'] + "@" + env["RABBITMQ_HOST"] +
                     ":" + env["RABBITMQ_PORT"] + "/" + env["RABBITMQ_VHOST"])

CELERY_RESULT_BACKEND = f"{REDIS_URL}/{env['REDIS_CELERY_RESULT_BACKEND_DB']}"

# Custom Settings
EMAIL_FROM = env["EMAIL_FROM"]
EMAIL_TO = env["EMAIL_TO"]

if settings.DEBUG:
    logger.debug("\nDjango settings:")
    for setting in dir(settings):
        if setting.isupper():
            value = getattr(settings, setting)
            logger.debug(f"{setting} = {value}")
