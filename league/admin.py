from django.contrib import admin
from .models import League

# Register your models here.
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('LEAGUE_ID', 'LOGO', 'TOTAL_CLUB', 'ASSOCIATION', 'FOUNDED', 'START_TIME', 'END_TIME')

admin.site.register(League, LeagueAdmin)
