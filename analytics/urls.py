from django.urls import path
from . import views as viewone
from django.contrib.auth import views

app_name = 'analytics'

urlpatterns = [
    path('', viewone.home, name = 'home'),
    path('index/', viewone.index, name = 'index'),
]