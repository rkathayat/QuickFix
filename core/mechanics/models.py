from django.db import models
from users.models import User

class Specialty(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialties = models.ManyToManyField(Specialty)
    years_of_experience = models.PositiveIntegerField()
    certification = models.CharField(max_length=100, blank=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.user.username