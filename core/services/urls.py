from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_service_request, name='create_service_request'),
    path('<int:pk>/', views.service_request_detail, name='service_request_detail'),
]