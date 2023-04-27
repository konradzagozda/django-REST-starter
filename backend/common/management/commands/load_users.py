import os
from django.core.management.base import BaseCommand, CommandError
import json
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Load users from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--file-path', type=str, help='Path to the JSON file containing users')

    def handle(self, *args, **options):
        file_path = options.get('file_path') or 'common/fixtures/users.json'

        if not os.path.exists(file_path):
            raise CommandError(f'File not found: {file_path}')

        with open(file_path, 'r') as file:
            users_data = json.load(file)

        for user_data in users_data:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                is_staff=user_data.get('is_staff', False),
                is_active=user_data.get('is_active', True),
                is_superuser=user_data.get('is_superuser', False)
            )
            user.set_password(user_data['password'])
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(users_data)} users'))
