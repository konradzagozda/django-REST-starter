from django.conf import settings
from django.contrib.auth.models import User
import pytest
from todo.models import Todo
from todo.tasks import send_undone_todos_email
from django.core import mail

pytestmark = pytest.mark.django_db

class TestUndoneTodos:
	def test_send_undone_todos_email_no_todos(self):
		user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')

		Todo.objects.create(user=user, title='Todo 1', description='Test todo 1', completed=True)
		Todo.objects.create(user=user, title='Todo 2', description='Test todo 2', completed=True)

		# Call the Celery task (using .apply() to call it synchronously)
		send_undone_todos_email.apply(args=[user.id])

		assert len(mail.outbox) == 0

	def test_send_undone_todos_email(self):
		user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')

		Todo.objects.create(user=user, title='Todo 1', description='Test todo 1')
		Todo.objects.create(user=user, title='Todo 2', description='Test todo 2', completed=True)
		Todo.objects.create(user=user, title='Todo 3', description='Test todo 3')

		# Call the Celery task (using .apply() to call it synchronously)
		send_undone_todos_email.apply(args=[user.id])

		assert len(mail.outbox) == 1

		email = mail.outbox[0]
		assert email.subject == 'Your Undone Todos'
		assert email.from_email == settings.EMAIL_FROM
		assert email.to == ['testuser@example.com']

		assert 'Todo 1' in email.body or 'Todo 1' in email.alternatives[0][0]
		assert 'Todo 3' in email.body or 'Todo 3' in email.alternatives[0][0]
		assert 'Todo 2' not in email.body and 'Todo 2' not in email.alternatives[0][0]
