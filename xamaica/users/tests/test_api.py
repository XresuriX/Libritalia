import pytest
from django.contrib.auth.models import User
from xamaica.users.models import User, Profile
from ninja_extra.testing import TestAsyncClient # type: ignore
from xamaica.users.api import app # Import the Ninja API instance

@pytest.mark.django_db
class TestProfileAPI:
    
    @pytest.fixture
    def user(self):
        return User.objects.create_user(username='testuser', password='password123')

    @pytest.fixture
    def profile(self, user):
        return Profile.objects.create(user=user, slug='testslug', bio='Test bio')

    @pytest.fixture
    def api_client(self):
        return TestAsyncClient(app)

    def test_get_profile(self, api_client, profile):
        response = api_client.get(f'/profiles/{profile.slug}/')
        assert response.status_code == 200
        assert response.json() == {
            'user': profile.user.id,
            'slug': profile.slug,
            'bio': profile.bio,
            'location': profile.location,
            'birth_date': profile.birth_date,
            'avatar': profile.avatar.url if profile.avatar else None,
            'about': profile.about,
        }

    def test_get_all_profiles(self, api_client, profile):
        response = api_client.get('/profiles/')
        assert response.status_code == 200
        profiles = response.json()
        assert len(profiles) == 1
        assert profiles[0]['slug'] == profile.slug

    def test_get_profile_not_found(self, api_client):
        response = api_client.get('/profiles/nonexistentslug/')
        assert response.status_code == 404