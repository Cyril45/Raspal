"""Contain super user creation functionality for user account administration on website."""

from django.core.management.base import BaseCommand
from account.models import MyUser


class Command(BaseCommand):
    """Here are defined the methods that can be used to create a super user."""

    def create_user(self):
        """Create a super user."""
        username = input("Votre nom d'utilisateur: ")
        email = input("Votre adresse email: ")
        password = input("Votre mot de passe: ")
        user = MyUser.objects.create_user(username, email, password)
        user.last_name = input("Votre nom de famille: ")
        user.first_name = input("Votre prénom: ")
        user.is_superuser = True
        user.save()
        print("Votre compte vient d'être créé")

    def handle(self, *args, **options):
        """Orders that are launched by Django."""
        self.create_user()
