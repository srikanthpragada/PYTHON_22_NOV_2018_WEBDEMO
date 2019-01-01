from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def list(request):
    con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    jobs = cur.fetchall()
    con.close()
    return render(request, 'list_jobs.html', {'jobs': jobs})


def add(request):
    return render(request, 'add_job.html')
