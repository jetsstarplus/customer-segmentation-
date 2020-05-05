"""ProjectY3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('analytics.urls')),
    path('admin/', admin.site.urls),
    path('login/',  auth_views.LoginView.as_view(template_name='analytics/login.html'), name = 'login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'analytics/logout.html'), name = 'logout'),
    path('reset/', auth_views.PasswordResetView.as_view(template_name = 'analytics/reset.html'), name = 'reset'),
    path('resetDone/', auth_views.PasswordResetDoneView.as_view(template_name = 'analytics/resetDone.html'), name = 'resetDone'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(template_name = 'analytics/resetConfirm.html'), name = 'resetConfirm'),
    path('index/', include('analytics.urls')),
]