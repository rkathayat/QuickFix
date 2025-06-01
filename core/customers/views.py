from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.models import ServiceRequest
from .models import Customer

@login_required
def customer_dashboard(request):
    if not hasattr(request.user, 'customer'):
        return redirect('home')
    
    customer = request.user.customer
    service_requests = ServiceRequest.objects.filter(
        customer=customer
    ).order_by('-created_at')
    
    context = {
        'active_requests': service_requests.exclude(status__in=['completed', 'cancelled']),
        'past_requests': service_requests.filter(status__in=['completed', 'cancelled']),
    }
    
    return render(request, 'customers/dashboard.html', context)