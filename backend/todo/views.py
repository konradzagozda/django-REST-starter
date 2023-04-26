from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
