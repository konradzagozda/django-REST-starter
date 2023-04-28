import pytest
from django.contrib.auth.models import User
from todo.serializers import TodoSerializer
from todo.models import Todo
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

@pytest.fixture
def test_user():
    return User.objects.create_user(username='test_user', password='test_password')

@pytest.fixture
def api_client():
    return APIClient()

class TestTodoModel:
    def test_todo_creation(self, test_user):
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

    def test_todo_completed(self, test_user):
        todo = Todo.objects.create(
            user=test_user,
            title='Test Todo',
            description='This is a test Todo item.',
            completed=True
        )

        assert todo.completed == True

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

class TestTodoViewSet:
    def test_todo_viewset_list(self, test_user, api_client):

        Todo.objects.create(user=test_user, title='Test Todo', description='This is a test Todo item.', completed=False)
        api_client.force_authenticate(user=test_user)

        response = api_client.get('/api/todos/')

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Test Todo'
        assert response.data[0]['description'] == 'This is a test Todo item.'
        assert response.data[0]['completed'] == False

    def test_todo_viewset_create(self, test_user, api_client):
        api_client.force_authenticate(user=test_user)

        response = api_client.post('/api/todos/', data={
            'title': 'Test Todo',
            'description': 'This is a test Todo item.',
            'completed': False,
        })

        assert response.status_code == 201
        assert response.data['title'] == 'Test Todo'
        assert response.data['description'] == 'This is a test Todo item.'
        assert response.data['completed'] == False

        todo = Todo.objects.first()
        assert todo.title == 'Test Todo'
        assert todo.description == 'This is a test Todo item.'
        assert todo.completed == False
