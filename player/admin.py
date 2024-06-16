from django.contrib import admin
from .models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('PLAYERID', 'PLAYERNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUB', 'IMAGE', 'CARDS', 'POSITION', 'SHIRTNUM', 'GOALS', 'ASSISTS', 'CONDITION', 'HEIGHT', 'WEIGHT', 'PREFERFOOT')

admin.site.register(Player, PlayerAdmin)