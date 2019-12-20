"""Contains the application’s url."""

from django.urls import path
from . import views

app_name = 'administration'
urlpatterns = [
    path('', views.index, name='index'),
    path('remove_user/<int:id_user>', views.remove_user, name='remove_user'),
    path('creating_user', views.creating_user, name='creating_user'),
]
