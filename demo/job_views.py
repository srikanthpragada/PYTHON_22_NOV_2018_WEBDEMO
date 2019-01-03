from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import JobForm
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
        f = JobForm()
        return render(request, 'add_job.html', {'form': f})
    else:
        f = JobForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            minsal = f.cleaned_data['minsal']
            maxsal = f.cleaned_data['maxsal']
            if minsal > maxsal:
                return render(request, 'add_job.html',
                              {'form': f, 'message': 'Min Salary must be <= Max Salary'})

            con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
            cur = con.cursor()
            cur.execute("insert into jobs(title,minsal,maxsal) values(?,?,?)",
                        (title, minsal, maxsal))
            con.commit()
            con.close()
            if cur.rowcount == 1:
                return redirect('/demo/listjobs')
            else:
                return render(request, 'add_job.html', {'form': f,
                                                        'message': 'Sorry! Could not add job!'})
        else:
            return render(request, 'add_job.html', {'form': f})


def delete_job(request, jobid):
    try:
        con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
        cur = con.cursor()
        cur.execute("delete from jobs where id = ?", (jobid,))
        if cur.rowcount == 1:
            con.commit()
            return redirect("/demo/listjobs")
    finally:
        con.close()

    return render(request, 'delete_job.html', {'jobid': jobid})


def edit_job(request, jobid):
    try:
        con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
        cur = con.cursor()
        cur.execute("select title,minsal,maxsal from jobs where id = ?", (jobid,))
        job = cur.fetchone()
        if job is None:
            return render(request, 'edit_job.html',
                          {'message': f"Job id {jobid} not found!"})
        else:
            form = JobForm({'title': job[0], 'minsal': job[1], 'maxsal': job[2]})
            return render(request, 'edit_job.html',
                          {'form' : form , 'jobid' : jobid})
    finally:
        con.close()


def update_job(request, jobid):
    try:
        con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
        cur = con.cursor()

        title = request.POST['title']
        minsal = int(request.POST['minsal'])
        maxsal = int(request.POST['maxsal'])
        if minsal > maxsal:
            raise ValueError('Minsal must be <= MaxSal')

        cur.execute("update jobs set title = ?, minsal = ?, maxsal=? where id = ?",
                    (title, minsal, maxsal, jobid))

        if cur.rowcount == 1:
            con.commit()
            return redirect("/demo/listjobs")
    except Exception as ex:
        form = JobForm({'title': title, 'minsal': minsal, 'maxsal': maxsal})
        return render(request, 'edit_job.html',
                      {'form': form, 'jobid': jobid ,'error' : ex})
    finally:
        con.close()