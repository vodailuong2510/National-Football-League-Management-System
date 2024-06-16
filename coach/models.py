from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Coach(models.Model):
    COACHID = models.CharField(primary_key = True, max_length=3)
    COACHNAME = models.CharField(max_length=30)
    BIRTHDAY = models.DateField()
    NATIONALITY = models.CharField(max_length=20)
    CLUB = models.CharField(max_length=30)
    IMAGE = models.ImageField(upload_to='images/')
    CARDS = models.CharField(max_length=6, default='None', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)