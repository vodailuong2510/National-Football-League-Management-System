# Generated by Django 5.0.6 on 2024-06-17 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_followers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following_player', to=settings.AUTH_USER_MODEL),
        ),
    ]