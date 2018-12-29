from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('topics/', views.topics),
    path('countries/', views.countries),
    path('country/', views.country),
    path('country_info/', views.country_info),
    path('factorial/', views.factorial),
]
