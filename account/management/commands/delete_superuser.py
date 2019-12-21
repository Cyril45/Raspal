"""Contain super user delete functionality for user account administration on website."""

from django.core.management.base import BaseCommand
from account.models import MyUser


class Command(BaseCommand):
    """Here are defined the methods that can be used to delete a super user."""

    def delete_user(self):
        """Delete a super user."""
        list_user = MyUser.objects.filter(is_superuser=True)
        print("Voici la liste des administrateurs")
        for username in list_user:
            print(username)

        username_select = input("Merci d'insérer le nom d'utilisateur que vous voulez supprimer: ")
        try:
            user_delete = MyUser.objects.get(username=username_select)
            user_delete.delete()
            print"L'utilisateur "+username_select+" a bien été supprimer")
        except MyUser.DoesNotExist:
            print("Ce nom d'utilisateur n'existe pas.")

    def handle(self, *args, **options):
        """Orders that are launched by Django."""
        self.delete_user()
