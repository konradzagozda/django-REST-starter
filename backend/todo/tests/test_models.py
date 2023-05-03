import pytest
from todo.models import Todo

pytestmark = pytest.mark.django_db


class TestTodoModel:

    def test_todo_creation(self, test_user):
        todo = Todo.objects.create(user=test_user,
                                   title='Test Todo',
                                   description='This is a test Todo item.',
                                   completed=False)

        assert todo.user == test_user
        assert todo.title == 'Test Todo'
        assert todo.description == 'This is a test Todo item.'
        assert todo.completed == False
        assert str(todo) == 'Test Todo'

    def test_todo_completed(self, test_user):
        todo = Todo.objects.create(user=test_user,
                                   title='Test Todo',
                                   description='This is a test Todo item.',
                                   completed=True)

        assert todo.completed == True
