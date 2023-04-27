import pytest
from django.contrib.auth.models import User
from .models import Todo

pytestmark = pytest.mark.django_db

# test models
@pytest.fixture
def test_user():
    return User.objects.create_user(username='test_user', password='test_password')

def test_todo_creation(test_user):
    todo = Todo.objects.create(
        user=test_user,
        title='Test Todo',
        description='This is a test Todo item.',
        completed=False
    )

    assert todo.user == test_user
    assert todo.title == 'Test Todo'
    assert todo.description == 'This is a test Todo item.'
    assert todo.completed == False
    assert str(todo) == 'Test Todo'

def test_todo_completed(test_user):
    todo = Todo.objects.create(
        user=test_user,
        title='Test Todo',
        description='This is a test Todo item.',
        completed=True
    )

    assert todo.completed == True
