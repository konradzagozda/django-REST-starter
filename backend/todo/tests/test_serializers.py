import pytest
from todo.models import Todo
from todo.serializers import TodoSerializer

pytestmark = pytest.mark.django_db

class TestTodoSerializer:
    def test_todo_serializer(self, test_user):
            todo = Todo.objects.create(
                title='Test Title',
                description='Test Description',
                completed=False,
                user=test_user
            )

            serializer = TodoSerializer(todo)

            assert serializer.data == {
                'id': todo.id,
                'title': 'Test Title',
                'description': 'Test Description',
                'completed': False
            }
