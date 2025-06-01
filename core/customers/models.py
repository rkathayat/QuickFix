from django.db import models
from users.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    preferred_contact_method = models.CharField(
        max_length=10,
        choices=[('phone', 'Phone'), ('email', 'Email'), ('app', 'In-app Messaging')],
        default='phone'
    )
    
    def __str__(self):
        return self.user.username