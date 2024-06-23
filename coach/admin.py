from django.contrib import admin
from .models import Coach

# Register your models here.
class CoachAdmin(admin.ModelAdmin):
    list_display = ('COACHID', 'COACHNAME', 'BIRTHDAY', 'NATIONALITY', 'CLUBID', 'IMAGE')

admin.site.register(Coach, CoachAdmin)