from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from mechanics.models import Specialty

class CustomerRegistrationForm(UserCreationForm):
    preferred_contact_method = forms.ChoiceField(
        choices=[('phone', 'Phone'), ('email', 'Email'), ('app', 'In-app Messaging')],
        widget=forms.RadioSelect
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2', 'preferred_contact_method']

class MechanicRegistrationForm(UserCreationForm):
    specialties = forms.ModelMultipleChoiceField(
        queryset=Specialty.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    years_of_experience = forms.IntegerField(min_value=0)
    hourly_rate = forms.DecimalField(min_value=0)
    certification = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2', 
                 'specialties', 'years_of_experience', 'hourly_rate', 'certification']