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
    STADIUM = models.CharField(max_length=100)
    CAPACITY = models.PositiveIntegerField()
    TOTALPLAYERS = models.PositiveIntegerField()
    LEAGUEPLAYING = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    followers = models.ManyToManyField(User, related_name='following_club', blank=True)

    def __str__(self):
        return self.CLUBNAME
    def formatted_founded(self):
        return self.FOUNDED.strftime('%d/%m/%Y')