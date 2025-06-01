from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.mechanic_dashboard, name='mechanic_dashboard'),
    path('request/<int:pk>/accept/', views.accept_request, name='accept_request'),
]