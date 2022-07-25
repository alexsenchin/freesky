from django.shortcuts import render, get_object_or_404
from requests import request
from . import models
from .models import News, MainCarousel, MainActivity


def main(request):
    all_mainactivity = models.MainActivity.objects.all()
    all_maincarousel = models.MainCarousel.objects.all()
    context = {'all_maincarousel': all_maincarousel, 
    'all_mainactivity': all_mainactivity}
    return render(request, 'news/main.html', context=context)

def news(request):
    all_news = models.News.objects.all()
    context = {'all_news': all_news}
    return render(request, 'news/news.html', context=context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})

def donations(request):
    all_donations = models.Donation.objects.all()
    context= {'all_donations': all_donations}
    return render(request, 'news/donations.html', context=context)

def projects(request):
    all_projects = models.Projects.objects.all()
    context= {'all_projects': all_projects}
    return render(request, 'news/projects.html', context=context)

def contacts(request):
    return render(request, 'news/contact.html')