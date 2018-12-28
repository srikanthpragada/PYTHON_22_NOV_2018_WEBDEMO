import requests
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>Demo Application</h1>")


def topics(request):
    return render(request, 'topics.html',
                  {'duration': 40,
                   'fee': 4000})  # request, template


def countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    return render(request, 'countries.html', {'countries': resp.json()})


def india(request):
    pass
