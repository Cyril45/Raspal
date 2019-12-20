"""Contain the application models."""
from django.db import models


class Savinvideo(models.Model):
    """Contain video recorded information."""

    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
