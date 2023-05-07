"""
This module provides project-wide fixtures for pytest
"""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def test_user():
    """create test user

    Returns:
        User: test user
    """
    return User.objects.create_user(username='test_user',
                                    password='test_password')


@pytest.fixture
def api_client() -> APIClient:
    """create rest framework APIClient

    Returns:
        APIClient: rest framework api client
    """

    return APIClient()
