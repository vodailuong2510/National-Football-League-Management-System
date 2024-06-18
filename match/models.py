from django.db import models
from league.models import League
from club.models import Club
# Create your models here.
class Match(models.Model):
    MATCHID = models.CharField(primary_key=True, max_length=10)
    LEAGUEID = models.ForeignKey(League, on_delete=models.CASCADE)
    HOMETEAM = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_team')
    AWAYTEAM = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_team')
    ROUND = models.PositiveIntegerField()
    DATE = models.DateField()
    TIME = models.TimeField()
    STADIUM = models.CharField(max_length=100)
    REFEREE = models.CharField(max_length=100)
    HOMESCORE = models.PositiveIntegerField(null=True, blank=True)
    AWAYSCORE = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.HOMETEAM} vs {self.AWAYTEAM}"
    def formatted_date(self):
        return self.DATE.strftime('%d/%m/%Y')
    def formatted_time(self):
        return self.TIME.strftime('%H:%M')
    
class Ranking(models.Model):
    LEAGUE = models.ForeignKey(League, on_delete=models.CASCADE)
    CLUB = models.ForeignKey(Club, on_delete=models.CASCADE)
    PLAYED = models.PositiveIntegerField(default=0)
    WON = models.PositiveIntegerField(default=0)
    DRAWN = models.PositiveIntegerField(default=0)
    LOST = models.PositiveIntegerField(default=0)
    GOALS_FOR = models.PositiveIntegerField(default=0)
    GOALS_AGAINST = models.PositiveIntegerField(default=0)
    GOAL_DIFFERENCE = models.IntegerField(default=0)
    POINTS = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('LEAGUE', 'CLUB')
        ordering = ['-POINTS', '-GOAL_DIFFERENCE', '-GOALS_FOR']