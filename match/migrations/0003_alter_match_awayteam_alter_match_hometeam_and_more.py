# Generated by Django 5.0.6 on 2024-06-16 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_alter_club_clubid_alter_club_leagueplaying'),
        ('league', '0002_league_logo_alter_league_association'),
        ('match', '0002_rename_awayid_match_awayteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='AWAYTEAM',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='club.club'),
        ),
        migrations.AlterField(
            model_name='match',
            name='HOMETEAM',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='club.club'),
        ),
        migrations.AlterField(
            model_name='match',
            name='LEAGUEID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.league'),
        ),
    ]
