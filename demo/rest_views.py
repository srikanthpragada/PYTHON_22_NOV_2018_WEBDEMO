from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demo.models import Job
from demo.serializers import JobSerializer


def job_client(request):
    return render(request, 'rest_client.html')


@api_view(['GET', 'POST'])
def job_process(request):
    if request.method == "GET":
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    else:  # POST
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)  # Bad request


@api_view(['GET', 'DELETE'])
def one_job_process(request, id):
    try:
        job = Job.objects.get(id=id)
    except:
        return Response(status=404)  # Send 404 to client

    if request.method == "GET":
        serializer = JobSerializer(job)
        return Response(serializer.data)
    else:
        job.delete()
        return Response(status=204)  # No content
