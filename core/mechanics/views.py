from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import ServiceRequest

@login_required
def mechanic_dashboard(request):
    if not hasattr(request.user, 'mechanic'):
        return redirect('home')
    
    mechanic = request.user.mechanic
    service_requests = ServiceRequest.objects.filter(
        mechanic=mechanic
    ).order_by('-created_at')
    
    new_requests = ServiceRequest.objects.filter(
        service_type__in=[s.name for s in mechanic.specialties.all()],
        status='pending',
        mechanic__isnull=True
    )
    
    context = {
        'active_requests': service_requests.exclude(status__in=['completed', 'cancelled']),
        'completed_requests': service_requests.filter(status='completed'),
        'new_requests': new_requests,
    }
    
    return render(request, 'mechanics/dashboard.html', context)

@login_required
def accept_request(request, pk):
    if not hasattr(request.user, 'mechanic'):
        return redirect('home')
    
    service_request = get_object_or_404(ServiceRequest, pk=pk, status='pending')
    service_request.mechanic = request.user.mechanic
    service_request.status = 'accepted'
    service_request.save()
    
    return redirect('mechanic_dashboard')