import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from todo.models import Todo
from todo.tasks import (create_random_users_and_tasks,
                        send_undone_todos_email_to_all_users)

pytestmark = pytest.mark.django_db


class TestUndoneTodos:

    def test_send_undone_todos_email_no_todos(self):
        user = User.objects.create_user(username='testuser',
                                        email='testuser@example.com',
                                        password='testpassword')

        Todo.objects.create(user=user,
                            title='Todo 1',
                            description='Test todo 1',
                            completed=True)
        Todo.objects.create(user=user,
                            title='Todo 2',
                            description='Test todo 2',
                            completed=True)

        # Call the Celery task (using .apply() to call it synchronously)
        send_undone_todos_email_to_all_users.apply()

        assert len(mail.outbox) == 0

    def test_send_undone_todos_email(self):
        user = User.objects.create_user(username='testuser',
                                        email='testuser@example.com',
                                        password='testpassword')

        Todo.objects.create(user=user,
                            title='Todo 1',
                            description='Test todo 1')
        Todo.objects.create(user=user,
                            title='Todo 2',
                            description='Test todo 2',
                            completed=True)
        Todo.objects.create(user=user,
                            title='Todo 3',
                            description='Test todo 3')

        send_undone_todos_email_to_all_users.apply()

        assert len(mail.outbox) == 1

        email = mail.outbox[0]
        assert email.subject == 'Your Undone Todos'
        assert email.from_email == settings.EMAIL_FROM
        assert email.to == ['testuser@example.com']

        assert 'Todo 1' in email.body or 'Todo 1' in email.alternatives[0][0]
        assert 'Todo 3' in email.body or 'Todo 3' in email.alternatives[0][0]
        assert 'Todo 2' not in email.body and 'Todo 2' not in email.alternatives[
            0][0]


class TestCreateRandomUsersAndTasks:

    def test_create_random_users_and_tasks(self):
        num_users = 10
        num_todos_per_user = 5

        create_random_users_and_tasks.apply(args=(num_users,
                                                  num_todos_per_user))

        assert User.objects.count() == num_users
        assert Todo.objects.count() == num_users * num_todos_per_user

        for user in User.objects.all():
            todos = Todo.objects.filter(user=user)
            assert todos.count() == num_todos_per_user

        assert len(mail.outbox) == 1

        email = mail.outbox[0]
        assert email.subject == 'Random users and tasks created'
        assert email.from_email == settings.EMAIL_FROM
        assert email.to == [settings.EMAIL_TO]

        message = f'Created {num_users} random users, each with {num_todos_per_user} tasks.'
        assert message in email.body
