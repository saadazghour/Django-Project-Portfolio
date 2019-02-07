from django.shortcuts import render
from .models import Job

# Create your views here.
def Home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs})
