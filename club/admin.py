from django.contrib import admin
from .models import Club
# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = ('CLUBID', 'CLUBNAME', 'LOGO', 'FOUNDED', 'EMAIL', 'PHONE', 'COACH', 'CAPTAIN', 'STADIUM', 'CAPACITY', 'TOTALPLAYERS', 'LEAGUEPLAYING')
    
admin.site.register(Club, ClubAdmin)