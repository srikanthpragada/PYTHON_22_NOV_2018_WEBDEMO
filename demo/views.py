import requests
import math
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


def country(request):
    return render(request, 'country.html')


def factorial(request):
    if request.method == "GET":
        return render(request, 'factorial.html')
    else:  # POST
        number = int(request.POST['number'])
        fact = math.factorial(number)
        return render(request, 'factorial.html',
                      {'number': number, 'fact': fact})


def country_info(request):
    # get country info about country and send it to template
    code = request.GET['code']
    URL = "https://restcountries.eu/rest/v2/alpha/" + code
    resp = requests.get(URL)
    if resp.status_code != 200:
        return render(request, 'country_info.html')
    else:
        return render(request, 'country_info.html', {'country': resp.json()})
