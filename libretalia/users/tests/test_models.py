import pytest
from django.test import RequestFactory
from allauth.account.signals import user_signed_up

from xamaica.users.models import Profile
from xamaica.users.models import User


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"


@pytest.mark.django_db()
def test_profile_creation_on_user_signup():
    user = User.objects.create_user(username="testuser", password="password123")  # noqa: S106
    assert user.get_absolute_url() == f"/users/{user.username}/"


@pytest.mark.django_db
def test_create_user_profile_signal():
    # Create a request factory
    factory = RequestFactory()

    # Create a user
    user = User.objects.create_user(username="testuser", password="password123")  # noqa: S106

    # Trigger the user_signed_up signal
    request = factory.post('/accounts/signup/')
    user_signed_up.send(sender=User, request=request, user=user)
    
    # Refresh from DB to ensure related objects are loaded
    user.refresh_from_db()

    # Ensure the user has an associated profile 
    assert hasattr(user, 'profile'), "Profile was not created for the user"
    assert user.profile.user == user
    print(user.profile.user.username)
    print(type(user.profile.user.username))

    # Ensure the profile is correctly linked to the user
    assert Profile.objects.get(user=user) == user.profile
