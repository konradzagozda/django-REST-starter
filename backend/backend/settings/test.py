from .base import *


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