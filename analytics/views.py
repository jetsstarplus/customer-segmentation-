from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'analytics/home.html')

# http://data.world/victorotieno
@login_required(login_url = 'login')
def index(request):

    return render(request,'analytics/dashboard-2.html')





