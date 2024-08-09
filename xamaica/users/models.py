from django.contrib.auth.models import AbstractUser  # noqa: EXE002
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

class User(AbstractUser):
    """
    Default custom user model for xamaica.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True,
    )
    avatar = models.ImageField(default="default.jpg", upload_to="profile_pics")
    about = models.TextField(_("about"), max_length=500, blank=True)
    slug = AutoSlugField(populate_from='user')  
    location = models.TextField(_("location"), max_length=50, blank=True)
    def __str__(self):
        return self.user.username

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
