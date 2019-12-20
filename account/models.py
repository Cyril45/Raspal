"""Contain the application models."""
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """Contain user information."""

    first_connexion = models.BooleanField(default=True)
