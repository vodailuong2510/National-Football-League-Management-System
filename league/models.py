from django.db import models

# Create your models here.
class League(models.Model):
    LEAGUE_ID = models.CharField(primary_key=True, max_length=3)
    LEAGUE_NAME = models.CharField(max_length=30)
    TOTAL_CLUB = models.IntegerField(default=0)
    ASSOCIATION = models.CharField(max_length=20)
    FOUNDED = models.DateField()
    START_TIME = models.DateField()
    END_TIME = models.DateField()
    IMAGE = models.ImageField(upload_to='league_images/', null=True, blank=True)

    def __str__(self):
        return self.LEAGUE_NAME
