from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    return HttpResponse("Hello")


def Drinks(request):
    return render(request, 'Drinks/drinks.html', {'data': 'test-data'})













