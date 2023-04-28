import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.fixture
def test_user():
    return User.objects.create_user(username='test_user', password='test_password')

@pytest.fixture
def api_client():
    return APIClient()
