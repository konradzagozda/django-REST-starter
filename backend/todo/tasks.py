from celery import shared_task
from todo.models import Todo
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def send_undone_todos_email(user_id):
    user = User.objects.get(id=user_id)
    todos = Todo.objects.filter(user=user, completed=False)

    if not todos:
        return

    subject = 'Your Undone Todos'
    from_email = settings.EMAIL_FROM
    to_email = user.email

    text_template = get_template('email/undone_todos.txt')
    html_template = get_template('email/undone_todos.html')

    context = {'user': user, 'todos': todos}

    text_content = text_template.render(context)
    html_content = html_template.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
