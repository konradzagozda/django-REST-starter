from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import get_template
from faker import Faker
from todo.models import Todo


@shared_task
def send_undone_todos_email_to_all_users() -> None:
    """
    send undone todos to all of the users
    """
    users = User.objects.all()

    for user in users:
        todos = Todo.objects.filter(user=user, completed=False)

        if not todos:
            continue

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


@shared_task
def create_random_users_and_tasks(num_users: int = 1000, num_todos_per_user: int = 100) -> None:
    """create random users and tasks

    Args:
        num_users (int, optional): number of users generated. Defaults to 1000.
        num_todos_per_user (int, optional): number of todos generated for a user. Defaults to 100.
    """
    fake = Faker()

    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        user = User.objects.create_user(username=username, email=email, password=password)

        for _ in range(num_todos_per_user):
            title = fake.sentence(nb_words=3)
            description = fake.text(max_nb_chars=200)
            completed = fake.boolean(chance_of_getting_true=50)

            Todo.objects.create(user=user, title=title, description=description, completed=completed)

    subject = 'Random users and tasks created'
    message = f'Created {num_users} random users, each with {num_todos_per_user} tasks.'

    send_mail(
        subject,
        message,
        settings.EMAIL_FROM,  # Replace with your 'from' email address
        [settings.EMAIL_TO],  # Replace with the admin's email address
    )
