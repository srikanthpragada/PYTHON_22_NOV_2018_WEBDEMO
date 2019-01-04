from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime


def list_movies(request):
    # find out city of the client
    if 'city' in request.COOKIES:
        cityname = request.COOKIES['city']
        return render(request, 'list_movies.html', {'city': cityname})
    else:
        return redirect("/demo/selectcity")


def select_city(request):
    if request.method == "GET":
        return render(request,'select_city.html')
    else:
        cityname = request.POST['city']
        response = HttpResponseRedirect("/demo/movies")
        response.set_cookie('city',cityname,
                expires = datetime.datetime.now() + datetime.timedelta(days=7))
        return response
