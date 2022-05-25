from multiprocessing import context
from django.shortcuts import render
from requests import request
from . import models

# Create your views here.
def news(request):
    all_news = models.News.objects.all()
    context = {'all_news': all_news}
    return render(request, 'news/news.html', context=context)

def donations(request):
    all_donations = models.Donation.objects.all()
    context= {'all_donations': all_donations}
    return render(request, 'news/donations.html', context=context)

def contacts(request):
    return render(request, 'news/contact.html')