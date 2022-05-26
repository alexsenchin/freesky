from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name='news'),
    path('', views.donations, name='donations'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts')
]