from django.urls import path
from . import views

app_name = 'tips'
urlpatterns = [
    path('', views.TipListView.as_view(), name='list'),
    path('<pk>/detail', views.TipDetailView.as_view(), name='detail'),
]