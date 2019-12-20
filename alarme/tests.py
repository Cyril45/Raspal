"""Django test module."""

from django.test import TestCase
from alarme.models import Savinvideo
import datetime
from account.models import MyUser
from django.conf import settings
import os

# test models
class SavinvideoTestCase(TestCase):
    def setUp(self):
        Savinvideo.objects.create(name="FakeVideoTest.mp4")

    def test_video_create(self):
        video =  Savinvideo.objects.get(name="FakeVideoTest.mp4")
        self.assertIsInstance(video.date, datetime.datetime)
        self.assertIsInstance(video.name, str)


# test view for ap alarme
class ViewPageTestCase(TestCase):
    def setUp(self):
        # create user admin
        userAdmin = MyUser.objects.create_user(
            "admin",
            "admin@admin.fr",
            "password"
            )
        userAdmin.last_name = "simonin"
        userAdmin.first_name = "cyril"
        userAdmin.is_superuser = True
        userAdmin.save()

         # create user
        user = MyUser.objects.create_user(
            "cyril",
            "cyril@email.fr",
            "password"
            )
        user.last_name = "simonin"
        user.first_name = "cyril"
        user.save()


        # create video
        Savinvideo.objects.create(name="FakeVideoTest.mp4")
        settings.MEDIA_ROOT+'/FakeVideoTest.mp4'
        os.system('touch {}'.format(settings.MEDIA_ROOT+'/FakeVideoTest.mp4'))

    def test_live_page(self):
        response = self.client.get('/views_live')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/views_live')
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_alarme_page(self):
        response = self.client.get('/alarme/activate')
        response2 = self.client.get('/alarme/desactivate')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/alarme/activate')
        response2 = self.client.get('/alarme/desactivate')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 302)

    def test_enregistrement_page(self):
        response = self.client.get('/enregistrement')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/enregistrement')
        self.assertEqual(response.status_code, 200)

    def test_download_pag(self): #creat fil avant
        response = self.client.get('/download/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/download/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 200)
    
    def test_view_vid_page(self):
        response = self.client.get('/view_vid/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/view_vid/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 200)

    def test_delete_vid_page(self):
        response = self.client.get('/delete_vid/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="cyril", password="password")
        response = self.client.get('/delete_vid/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 302)
        self.client.login(username="admin", password="password")
        response = self.client.get('/delete_vid/FakeVideoTest.mp4')
        self.assertEqual(response.status_code, 302)
    

