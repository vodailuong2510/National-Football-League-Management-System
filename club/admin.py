from django.contrib import admin
from .models import Club
# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = ('CLUBID', 'LOGO', 'FOUNDED', 'EMAIL', 'PHONE', 'STADIUM', 'CAPACITY', 'TOTALPLAYERS', 'LEAGUEPLAYING')
    
admin.site.register(Club, ClubAdmin)