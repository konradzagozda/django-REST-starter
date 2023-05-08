"""Todo package models."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Todo(models.Model):
    """Todo model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Representation of todo model."""
        return self.title
