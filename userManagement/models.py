from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    facialEmbedding = models.BinaryField(blank=True)