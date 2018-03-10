from django.urls import path
from . import views

app_name = 'tips'
urlpatterns = [
    path('', views.TipListView.as_view(), name='list'),
    path('<pk>', views.TipDetailView.as_view(), name='detail'),
    path('<pk>/edit', views.TipUpdateView.as_view(), name='update'),
    path('<pk>/delete', views.TipDeleteView.as_view(), name='delete'),
]