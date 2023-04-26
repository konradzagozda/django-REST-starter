from django.urls import path
from .views import TodoListCreateView

urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo_list_create'),
]
