from django.shortcuts import render
from django.http import HttpResponse
from .major_arcana import get_reading, get_reading_cards
# Create your views here.

def homePageView(request):
    return HttpResponse(get_reading())

def getReadingFromCards(request):
    return HttpResponse(get_reading_cards(request))

