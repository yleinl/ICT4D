"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from weather import views

urlpatterns = [
    path('agricultural_services/', views.agricultural_services, name='agricultural_services'),
    path('main_and_language/', views.main_and_language, name='main_and_language'),
    path('messaging_service/', views.messaging_service, name='messaging_service'),
    path('subscription_services/', views.subscription_services, name='subscription_services'),
    path('weather_reports/', views.weather_reports, name='weather_reports'),
]
