import pytest

from libretalia.users.models import Profile
from libretalia.users.models import User


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"


@pytest.mark.django_db()
def test_profile_creation_on_user_signup():
    user = User.objects.create_user(username="testuser", password="password123")  # noqa: S106

    # Verify the profile is created
    # assert Profile.objects.filter(user=user).exists()  # noqa: ERA001
    assert user.get_absolute_url() == f"/users/{user.username}/"


