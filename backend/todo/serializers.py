"""Todo package serializers."""
from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Todo serializer."""

    class Meta:
        """Metadata for todo serailizer."""

        model = Todo
        fields = ('id', 'title', 'description', 'completed')
