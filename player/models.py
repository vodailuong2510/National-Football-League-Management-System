from django.db import models

# Create your models here.
class Player(models.Model):
    PLAYERID = models.CharField(primary_key = True, max_length=3)
    PLAYERNAME = models.CharField(max_length=30)
    BIRTHDAY = models.DateField()
    NATIONALITY = models.CharField(max_length=20)
    CLUB = models.CharField(max_length=30)
    IMAGE = models.ImageField(upload_to='images/')
    CARDS = models.CharField(max_length=6, default='None', null=True, blank=True)