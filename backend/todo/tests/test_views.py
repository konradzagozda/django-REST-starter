"""
Test todo views
"""
import pytest
from todo.models import Todo

pytestmark = pytest.mark.django_db


class TestTodoViewSet:
    """
    Test todo views
    """

    def test_todo_viewset_list(self, test_user, api_client):
        """
        Test todo list view
        """
        Todo.objects.create(user=test_user,
                            title='Test Todo',
                            description='This is a test Todo item.',
                            completed=False)
        api_client.force_authenticate(user=test_user)

        response = api_client.get('/api/todos/')

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Test Todo'
        assert response.data[0]['description'] == 'This is a test Todo item.'
        assert response.data[0]['completed'] is False

    def test_todo_viewset_create(self, test_user, api_client):
        """
        Test todo create view
        """
        api_client.force_authenticate(user=test_user)

        response = api_client.post('/api/todos/',
                                   data={
                                       'title': 'Test Todo',
                                       'description': 'This is a test Todo item.',
                                       'completed': False,
                                   })

        assert response.status_code == 201
        assert response.data['title'] == 'Test Todo'
        assert response.data['description'] == 'This is a test Todo item.'
        assert response.data['completed'] is False

        todo = Todo.objects.first()
        assert todo.title == 'Test Todo'
        assert todo.description == 'This is a test Todo item.'
        assert todo.completed is False
