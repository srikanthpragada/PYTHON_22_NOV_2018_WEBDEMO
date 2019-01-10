from django.views.generic import TemplateView, ListView
from .models import Job


class AboutView(TemplateView):
    template_name = "about.html"


class JobsListView(ListView):
    model = Job
    template_name = 'jobs.html'
