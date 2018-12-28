from django.http import HttpResponse
from datetime import datetime


# Function view
def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def wish(request):
    # check whether name parameter is present in request
    if 'name' in request.GET:
        name = request.GET['name']  # name passed in querystring
    else:
        name = "Unknown"

    hours = datetime.now().hour  # hour of the day

    if hours < 12:
        message = "Good Morning!"
    elif hours < 17:
        message = "Good afternoon!"
    else:
        message = "Good Evening!"

    return HttpResponse(f"<h1 style='color:red'>{message} {name}</h1>")
