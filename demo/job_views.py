from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  AddJobForm
import sqlite3


def list(request):
    con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    jobs = cur.fetchall()
    con.close()
    return render(request, 'list_jobs.html', {'jobs': jobs})


def add(request):
    if request.method == "GET":
        f = AddJobForm()
        return render(request, 'add_job.html',{'form' : f})
    else:
        f = AddJobForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            minsal = f.cleaned_data['minsal']
            maxsal = f.cleaned_data['maxsal']
            if minsal > maxsal:
                return render(request, 'add_job.html', {'form': f,
                                    'message': 'Min Salary must be <= Max Salary'})

            con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
            cur = con.cursor()
            cur.execute("insert into jobs(title,minsal,maxsal) values(?,?,?)",
                        (title,minsal,maxsal))
            con.commit()
            con.close()
            if cur.rowcount == 1:
                return redirect('/demo/listjobs')
            else:
                return render(request, 'add_job.html', {'form': f,
                       'message' : 'Sorry! Could not add job'})
        else:
            return render(request, 'add_job.html', {'form': f})
