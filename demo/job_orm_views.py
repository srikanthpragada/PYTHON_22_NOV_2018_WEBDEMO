from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Job
from .forms import AddJobForm


def list_jobs(request):
    return render(request, 'orm_list_jobs.html',
                  {'jobs': Job.objects.all()})


def add_job(request):
    if request.method == "GET":
        return render(request, 'orm_add_job.html', {'form': AddJobForm()})
    else:
        form = AddJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/demo/orm/listjobs")
        else:
            return render(request, 'orm_add_job.html', {'form': form})


def delete_job(request, jobid):
    job = Job.objects.get(id=jobid)
    job.delete()
    return redirect("/demo/orm/listjobs")


def search_jobs(request):
    return render(request, 'orm_search_jobs.html')


def get_jobs(request):
    title = request.GET['title']
    # values() converts job object to dict
    jobs = Job.objects.filter(title__contains=title).values()
    jobslist = list(jobs)  # Convert QuerySet to list
    return JsonResponse(jobslist, safe=False)
