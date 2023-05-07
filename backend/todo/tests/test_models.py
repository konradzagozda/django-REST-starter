"""
Test todo models
"""

import pytest
from django.contrib.auth import get_user_model
from todo.models import Todo

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestTodoModel:
    """
    Test todo models
    """

    def test_todo_creation(self, test_user: User):
        """Test create uncompleted todo

        Args:
            test_user (User): fixture created user
        """
        todo = Todo.objects.create(user=test_user,
                                   title='Test Todo',
                                   description='This is a test Todo item.',
                                   completed=False)

        assert todo.user == test_user
        assert todo.title == 'Test Todo'
        assert todo.description == 'This is a test Todo item.'
        assert todo.completed is False
        assert str(todo) == 'Test Todo'

    def test_todo_completed(self, test_user: User):
        """Test create completed todo

        Args:
            test_user (User): fixture created user
        """
        todo = Todo.objects.create(user=test_user,
                                   title='Test Todo',
                                   description='This is a test Todo item.',
                                   completed=True)

        assert todo.completed is True
