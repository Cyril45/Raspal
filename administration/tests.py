"""Django test module."""

from django.test import TestCase
from account.models import MyUser

# test view for ap administration
class ViewPageTestCase(TestCase):
    def setUp(self):
        # create admin user
        userAdmin = MyUser.objects.create_user(
            "cyril",
            "cyril@email.fr",
            "password"
            )
        userAdmin.last_name = "simonin"
        userAdmin.first_name = "cyril"
        userAdmin.is_superuser = True
        userAdmin.save()

         # create admin user basic
        userLambda = userAdmin = MyUser.objects.create_user(
            "cyrillambda",
            "cyrillambda@email.fr",
            "password"
            )
        userLambda.last_name = "cyrillambda"
        userLambda.first_name = "cyrillambda"
        userLambda.save()
        self.userLambda = userLambda

    def test_index_page(self):
        response = self.client.get('/administration/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyrillambda", password="password")
        response = self.client.get('/administration/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyril", password="password")
        response = self.client.get('/administration/')
        self.assertEqual(response.status_code, 200)
    
    def test_remove_user_page(self):
        response = self.client.get('/administration/remove_user/'+str(self.userLambda.id))
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyrillambda", password="password")
        response = self.client.get('/administration/remove_user/'+str(self.userLambda.id))
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyril", password="password")
        response = self.client.get('/administration/remove_user/'+str(self.userLambda.id))
        self.assertEqual(response.status_code, 302)
    
    def test_creating_user_page(self):
        response = self.client.get('/administration/creating_user')
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyrillambda", password="password")
        response = self.client.get('/administration/creating_user')
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyril", password="password")
        response = self.client.get('/administration/creating_user')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/administration/creating_user',
            {
                'username': 'john',
                'email': 'john@smith.fr',
                'last_name': 'smith',
                'first_name': 'john'
                }
            )
        self.assertEqual(response.status_code, 302)

