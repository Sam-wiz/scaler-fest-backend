from django.db import models

# Create your models here.
class EarlyInterest(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)