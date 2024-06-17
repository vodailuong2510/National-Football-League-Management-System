from django.db import models
from django.contrib.auth.models import User
class Player(models.Model):
    PLAYERID = models.CharField(primary_key=True, max_length=3)
    PLAYERNAME = models.CharField(max_length=30)
    BIRTHDAY = models.DateField()
    NATIONALITY = models.CharField(max_length=20)
    CLUB = models.CharField(max_length=30)
    IMAGE = models.ImageField(upload_to='images/')
    CARDS = models.CharField(max_length=6, default='None', null=True, blank=True)
    
    # Additional fields
    POSITION_CHOICES = [
        ('GK', 'Thủ môn'),
        ('DF', 'Hậu vệ'),
        ('MF', 'Tiền vệ'),
        ('FW', 'Tiền đạo'),
    ]
    POSITION = models.CharField(max_length=2, choices=POSITION_CHOICES, default='GK')
    SHIRTNUM = models.PositiveIntegerField(null = True, blank = True)
    GOALS = models.PositiveIntegerField(default=0, null=True, blank=True)
    ASSISTS = models.PositiveIntegerField(default=0, null=True, blank=True)
    CONDITION = models.CharField(max_length=20, default='Tốt')
    HEIGHT = models.DecimalField(max_digits=5, decimal_places=2, default=0.)  # in centimeters
    WEIGHT = models.DecimalField(max_digits=5, decimal_places=2, default=0.)  # in kilograms
    
    FOOT_CHOICES = [
        ('L', 'Chân trái'),
        ('R', 'Chân phải'),
        ('B', 'Cả hai chân'),
    ]
    PREFERFOOT = models.CharField(max_length=1, choices=FOOT_CHOICES, default='R')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return f"{self.PLAYERNAME} ({self.PLAYERID})"
