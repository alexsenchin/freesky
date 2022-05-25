from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('donations/', views.donations, name='donations'),
    path('contacts/', views.contacts, name='contacts')
]