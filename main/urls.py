from django.contrib import admin
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('company/', views.companylist, name="company"),
    path('reports/', views.reports, name="reports"),
    path('contact/', views.contact, name="contact"),
]