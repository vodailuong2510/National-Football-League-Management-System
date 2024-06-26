# Generated by Django 4.2.13 on 2024-06-23 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('MATCHID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ROUND', models.PositiveIntegerField()),
                ('DATE', models.DateField()),
                ('TIME', models.TimeField()),
                ('STADIUM', models.CharField(max_length=100)),
                ('REFEREE', models.CharField(max_length=100)),
                ('HOMESCORE', models.PositiveIntegerField(blank=True, null=True)),
                ('AWAYSCORE', models.PositiveIntegerField(blank=True, null=True)),
                ('AWAYTEAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='club.club')),
                ('HOMETEAM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='club.club')),
                ('LEAGUEID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.league')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PLAYED', models.PositiveIntegerField(default=0)),
                ('WON', models.PositiveIntegerField(default=0)),
                ('DRAWN', models.PositiveIntegerField(default=0)),
                ('LOST', models.PositiveIntegerField(default=0)),
                ('GOALS_FOR', models.PositiveIntegerField(default=0)),
                ('GOALS_AGAINST', models.PositiveIntegerField(default=0)),
                ('GOAL_DIFFERENCE', models.IntegerField(default=0)),
                ('POINTS', models.PositiveIntegerField(default=0)),
                ('CLUB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
                ('LEAGUE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.league')),
            ],
            options={
                'ordering': ['-POINTS', '-GOAL_DIFFERENCE', '-GOALS_FOR'],
                'unique_together': {('LEAGUE', 'CLUB')},
            },
        ),
    ]
