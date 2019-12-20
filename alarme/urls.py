"""Contains the application’s url."""

from django.urls import path
from . import views


app_name = 'alarme'
urlpatterns = [
    path('', views.index, name='index'),
    path('alarme/<str:receiv>', views.alarme, name='alarme'),
    path('enregistrement', views.enregistrement, name='enregistrement'),
    path('download/<str:namefile>', views.download, name='download'),
    path('view_vid/<str:namefile>', views.view_vid, name='view_vid'),
    path('delete_vid/<str:namefile>', views.delete_vid, name='delete_vid'),
    path('views_live', views.views_live, name='views_live'),
]
