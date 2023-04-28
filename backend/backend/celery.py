import os

from celery import Celery, shared_task
from django.conf import settings
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.base')

app = Celery('backend',)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'todo.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
