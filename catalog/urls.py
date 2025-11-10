from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.release_list, name='release_list'),
    path('<int:pk>/', views.release_detail, name='release_detail')
]