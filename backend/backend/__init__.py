"""Init backend package."""
from backend.celery import celery_app

__all__ = ('celery_app',)
