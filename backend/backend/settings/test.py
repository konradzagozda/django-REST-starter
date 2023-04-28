from backend.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': os.environ.get('DB_HOST', 'postgres'),
        'PORT': 5432,
    }
}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
