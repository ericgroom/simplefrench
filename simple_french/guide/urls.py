from django.urls import path
from . import views

app_name = 'guide'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='list'),
    path('<pk>', views.ArticleDetailView.as_view(), name='detail'),
]