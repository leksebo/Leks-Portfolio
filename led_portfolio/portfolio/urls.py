from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
