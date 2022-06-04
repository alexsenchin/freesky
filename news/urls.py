from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('', views.donations, name='donations'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts')
]