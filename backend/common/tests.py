import json
from io import StringIO

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError

User = get_user_model()

pytestmark = pytest.mark.django_db


@pytest.fixture
def users_data():
    return [{
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "password": "admin",
        "is_superuser": True
    }, {
        "username": "user1",
        "email": "user1@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "user1"
    }, {
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "Maria",
        "last_name": "Doe",
        "password": "user2"
    }, {
        "username": "user3",
        "email": "user3@example.com",
        "first_name": "Konrad",
        "last_name": "Doe",
        "password": "user3"
    }]


@pytest.fixture
def create_fixture_file(tmpdir, users_data):
    file_path = tmpdir.join('users.json')
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(users_data, file)
    return str(file_path)


def test_load_users_command(create_fixture_file, users_data):
    out = StringIO()
    call_command('load_users', '--file-path', create_fixture_file, stdout=out)

    assert User.objects.count() == len(users_data)

    for user_data in users_data:
        user = User.objects.get(username=user_data['username'])
        assert user.email == user_data['email']
        assert user.first_name == user_data['first_name']
        assert user.last_name == user_data['last_name']
        assert user.is_superuser == user_data.get('is_superuser', False)

    assert 'Successfully loaded 4 users' in out.getvalue()


def test_load_users_command_invalid_path():
    non_existent_file_path = 'non_existent_file.json'
    with pytest.raises(CommandError, match=f'File not found: {non_existent_file_path}'):
        call_command('load_users', '--file-path', non_existent_file_path)
