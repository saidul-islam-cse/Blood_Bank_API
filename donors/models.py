from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    
    BLOOD_GROUPS = [
        ('O+', 'O+'), ('O-', 'O-'),
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]
    
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    last_donation_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'DonorPorfile'