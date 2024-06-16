from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Club(models.Model):
    CLUBID = models.CharField(primary_key=True, max_length=3)
    CLUBNAME = models.CharField(max_length=100)
    LOGO = models.ImageField(upload_to='images/')
    FOUNDED = models.DateField()
    EMAIL = models.EmailField()
    PHONE = models.CharField(max_length=15)
    COACH = models.CharField(max_length=100)
    CAPTAIN = models.CharField(max_length=100)
    STADIUM = models.CharField(max_length=100)
    CAPACITY = models.PositiveIntegerField()
    TOTALPLAYERS = models.PositiveIntegerField()
    LEAGUEPLAYING = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)