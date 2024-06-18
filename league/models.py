from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class League(models.Model):
    LEAGUE_ID = models.CharField(primary_key=True, max_length=3)
    LEAGUE_NAME = models.CharField(max_length=30)
    TOTAL_CLUB = models.IntegerField(default=0)
    ASSOCIATION = models.CharField(max_length=20)
    FOUNDED = models.DateField()
    START_TIME = models.DateField()
    END_TIME = models.DateField()
    IMAGE = models.ImageField(upload_to='league/', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    followers = models.ManyToManyField(User, related_name='following_league', blank=True)

    def __str__(self):
        return self.LEAGUE_NAME
