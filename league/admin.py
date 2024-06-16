from django.contrib import admin
from .models import League

# Register your models here.
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('LEAGUE_ID', 'LEAGUE_NAME', 'TOTAL_CLUB', 'ASSOCIATION', 'FOUNDED', 'START_TIME', 'END_TIME', 'IMAGE')

admin.site.register(League, LeagueAdmin)
