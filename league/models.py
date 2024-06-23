from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class League(models.Model):
    LEAGUE_ID = models.CharField(primary_key=True, max_length=50)
    LOGO = models.ImageField(upload_to='league/', null = True)
    TOTAL_CLUB = models.IntegerField(default=0)
    ASSOCIATION = models.CharField(max_length=50)
    FOUNDED = models.DateField()
    START_TIME = models.DateField()
    END_TIME = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    followers = models.ManyToManyField(User, related_name='following_league', blank=True)

    def __str__(self):
        return self.LEAGUE_ID
    def formatted_founded(self):
        return self.FOUNDED.strftime('%d/%m/%Y')
    def formatted_start_time(self):
        return self.START_TIME.strftime('%d/%m/%Y')
    def formatted_end_time(self):
        return self.END_TIME.strftime('%d/%m/%Y')