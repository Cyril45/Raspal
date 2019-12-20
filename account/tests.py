"""Django test module."""

from django.test import TestCase
from account.models import MyUser

class ViewPageTestCase(TestCase):
    def setUp(self):
        # create user
        user = MyUser.objects.create_user(
            "cyril",
            "cyril@email.fr",
            "password"
            )
        user.last_name = "simonin"
        user.first_name = "cyril"
        user.save()

    def test_sign_in_page(self):
        response = self.client.get('/account/sign_in')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/account/sign_in', {'username': 'wrong', 'password': 'useruser'})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/account/sign_in', {'username': 'cyril', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
    
    def test_my_account_page(self):
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)
    
    def test_modif_account_page(self):
        response = self.client.get('/account/modif_account')
        self.assertEqual(response.status_code, 302)

        self.client.login(username="cyril", password="password")
        response = self.client.get('/account/modif_account')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/account/modif_account',
            {
                'username': 'cyril',
                'last_name': 'lastnameuser',
                'first_name': 'firstname_user',
                'email': 'email@email.fr'
                }
            )
        self.assertEqual(response.status_code, 302)
    
    def test_modif_password_page(self):
        response = self.client.get('/account/modif_password')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/account/modif_password')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            '/account/modif_password',
            {
                'old_password': 'password',
                'new_password': 'passwordpassword',
                'new_password_compare': 'passwordpassword'
                }
            )
        self.assertEqual(response.status_code, 302)

    def test_delete_account_page(self):
        response = self.client.get('/account/delete_account')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/account/delete_account')
        self.assertEqual(response.status_code, 302)
    
    def test_sign_out_page(self):
        response = self.client.get('/account/sign_out')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/account/sign_out')
        self.assertEqual(response.status_code, 302)
    
    def test_retrieve_password_page(self):
        response = self.client.get('/account/retrieve_password')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/account/retrieve_password', {'email': 'wrong@mail.fr'})
        self.assertEqual(response.status_code, 404)
        response = self.client.post('/account/retrieve_password', {'email': 'cyril@email.fr'})
        self.assertEqual(response.status_code, 302)



