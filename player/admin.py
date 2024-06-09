from django.contrib import admin
from .models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('PLAYERID', 'PLAYERNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUB', 'IMAGE')

admin.site.register(Player, PlayerAdmin)