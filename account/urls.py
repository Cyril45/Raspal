"""Contains the application’s url."""

from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('', views.my_account, name='my_account'),
    path('modif_account', views.modif_account, name='modif_account'),
    path('modif_password', views.modif_password, name='modif_password'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('sign_out', views.sign_out, name='sign_out'),
    path(
        'retrieve_password',
        views.retrieve_password,
        name='retrieve_password'),
]
