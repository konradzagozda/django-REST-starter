"""This module provides project-wide fixtures for pytest."""
from django.contrib.auth.models import User
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def test_user() -> User:
    """Fixture that returns test User."""
    return User.objects.create_user(username='test_user', password='test_password')


@pytest.fixture
def api_client() -> APIClient:
    """Fixture that returns rest framework APIClient."""
    return APIClient()
