from django.contrib import admin
from django.urls import path
from . import views, job_views

urlpatterns = [
    path('index/', views.index),
    path('topics/', views.topics),
    path('countries/', views.countries),
    path('country/', views.country),
    path('country_info/', views.country_info),
    path('factorial/', views.factorial),
    path('listjobs/', job_views.list),
    path('addjob/', job_views.add),
]
