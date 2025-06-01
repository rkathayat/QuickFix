from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomerRegistrationForm, MechanicRegistrationForm

def home(request):
    return render(request, 'users/home.html')
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            
            # Create customer profile
            customer = Customer.objects.create(
                user=user,
                preferred_contact_method=form.cleaned_data['preferred_contact_method']
            )
            
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('customer_dashboard')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'users/register_customer.html', {'form': form})

def register_mechanic(request):
    if request.method == 'POST':
        form = MechanicRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_mechanic = True
            user.save()
            
            # Create mechanic profile
            mechanic = Mechanic.objects.create(
                user=user,
                years_of_experience=form.cleaned_data['years_of_experience'],
                certification=form.cleaned_data['certification'],
                hourly_rate=form.cleaned_data['hourly_rate']
            )
            
            # Add specialties
            mechanic.specialties.set(form.cleaned_data['specialties'])
            
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('mechanic_dashboard')
    else:
        form = MechanicRegistrationForm()
    return render(request, 'users/register_mechanic.html', {'form': form})