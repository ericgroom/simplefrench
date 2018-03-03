from django.urls import path
from . import views

app_name = 'tips'
urlpatterns = [
    path('', views.index, name='tips-feed'),
]