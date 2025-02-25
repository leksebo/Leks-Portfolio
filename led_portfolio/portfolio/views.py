from django.shortcuts import render
from .models import PersonalInfo, Project

def landing(request):
    return render(request, 'portfolio/landing.html')


def home(request):
    personal_info = PersonalInfo.objects.first()
    featured_projects = Project.objects.filter(is_featured=True)
    return render(request, 'portfolio/home.html', {
        'personal_info': personal_info,
        'featured_projects': featured_projects
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {
        'projects': projects
    })

def contact(request):
    return render(request, 'portfolio/contact.html')
