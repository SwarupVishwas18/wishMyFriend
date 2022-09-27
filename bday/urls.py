from unicodedata import name
from django.urls import path
from . import views

app_name = 'bday'

urlpatterns = [
     path('', views.index, name='index'),
]