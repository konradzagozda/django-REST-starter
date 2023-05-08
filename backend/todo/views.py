"""Todo viewset."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Todo viewset."""

    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        """Get todo queryset filtered by request.user."""
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Override perform create to append user to todo object."""
        serializer.save(user=self.request.user)
