import pytest
from django.contrib.auth import get_user_model

from user.tests.factories import UserFactory


@pytest.mark.django_db
class TestUserModel:
    """Test cases for the User model."""

    def test_create_user(self):
        """Test creating a regular user."""
        user = UserFactory.create()  # Create a user instance using factory
        assert user.email is not None
        assert user.check_password('default_password')  # Ensure the password is checked against the default password

    def test_create_superuser(self):
        """Test creating a superuser."""
        superuser = get_user_model().objects.create_superuser(email='admin@example.com', password='password123')
        assert superuser.is_staff is True
        assert superuser.is_superuser is True

    def test_unique_email(self):
        """Test that email addresses are unique."""
        UserFactory.create(email='unique@example.com')
        with pytest.raises(Exception):  # Expect an error when creating a duplicate email
            UserFactory.create(email='unique@example.com')

    def test_str_representation(self):
        """Test the string representation of the user."""
        user = UserFactory.create(email='user@example.com')
        assert str(user) == 'user@example.com'
