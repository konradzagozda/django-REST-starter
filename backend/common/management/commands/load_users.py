import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Load users from a JSON file'

    def handle(self, *args, **options):
        file_path = 'common/fixtures/users.json'

        with open(file_path, 'r') as file:
            users_data = json.load(file)

        for user_data in users_data:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            user.set_password(user_data['password'])
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(users_data)} users'))
