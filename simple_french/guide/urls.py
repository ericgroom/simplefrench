from django.urls import path
from . import views

app_name = 'guide'

urlpatterns = [
    path('', views.article_table_of_contents, name='list'),
    path('<slug>', views.ArticleDetailView.as_view(), name='detail'),
]