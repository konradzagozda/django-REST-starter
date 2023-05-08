import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = os.environ

if env.get('LOADED') is None:
    print('Seems like environment file is not loaded')

# BEGIN DJANGO
DEBUG = env.get("DJANGO_DEBUG", "")
SECRET_KEY = env.get("DJANGO_SECRET_KEY", "")

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
        "NAME": env.get("DB_NAME", ""),
        "USER": env.get("DB_USER", ""),
        "PASSWORD": env.get("DB_PASSWORD", ""),
        "HOST": env.get("DB_HOST", ""),
        "PORT": 5432,
    }
}

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

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env.get("EMAIL_HOST", "")
EMAIL_PORT = env.get("EMAIL_PORT", "")
REDIS_URL = "redis://" + env.get("REDIS_USERNAME", "") + ":" + env.get("REDIS_PASSWORD", "") + \
            "@" + env.get("REDIS_HOST", "") + ":" + env.get("REDIS_PORT", "")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL + "/" + env.get("REDIS_CACHE_DB", ""),
    }
}

# END DJANGO

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.TokenAuthentication",],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated",],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SITE_ID = 1  # https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional

SPECTACULAR_SETTINGS = {  # drf-spectacular
    "TITLE": "Todo API",
    "DESCRIPTION": "Starter project",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# ALLAUTH
ACCOUNT_EMAIL_VERIFICATION = env.get("ACCOUNT_EMAIL_VERIFICATION", "")

CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 min task limit
CELERY_CACHE_BACKEND = "django-cache"

CELERY_BROKER_URL = ("amqp://" + env.get("RABBITMQ_USER", "") + ":" +
                     env.get('RABBITMQ_PASSWORD', "") + "@" + env.get("RABBITMQ_HOST", "") + ":" +
                     env.get("RABBITMQ_PORT", "") + "/" + env.get("RABBITMQ_VHOST", ""))

CELERY_RESULT_BACKEND = f"{REDIS_URL}/{env.get('REDIS_CELERY_RESULT_BACKEND_DB', '')}"

# Custom Settings
EMAIL_FROM = env.get("EMAIL_FROM", "")
EMAIL_TO = env.get("EMAIL_TO", "")
