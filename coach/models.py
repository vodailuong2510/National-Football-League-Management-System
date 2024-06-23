from django.db import models
from django.contrib.auth.models import User
from club.models import Club
# Create your models here.
class Coach(models.Model):
    COACHID = models.CharField(primary_key = True, max_length=3)
    COACHNAME = models.CharField(max_length=30)
    BIRTHDAY = models.DateField()
    NATIONALITY = models.CharField(max_length=20) 
    IMAGE = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    followers = models.ManyToManyField(User, related_name='following_coach', blank=True)
    CLUBID = models.OneToOneField(Club, to_field='CLUBID', on_delete=models.CASCADE, null = True, blank = True) 