from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_service_request(request):
    if not hasattr(request.user, 'customer'):
        return redirect('home')  # Or show error
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('service_request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    
    return render(request, 'services/create_request.html', {'form': form})

@login_required
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    # Check if user is authorized to view this request
    if not (request.user == service_request.customer.user or 
            (hasattr(request.user, 'mechanic') and request.user.mechanic == service_request.mechanic)):
        return redirect('home')
    
    return render(request, 'services/request_detail.html', {'request': service_request})