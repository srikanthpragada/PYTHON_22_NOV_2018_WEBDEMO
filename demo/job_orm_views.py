from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Job


def list(request):
    return render(request,'orm_list_jobs.html',
                  {'jobs': Job.objects.all()})


def add(request):
    pass

def delete_job(request, jobid):
    pass


