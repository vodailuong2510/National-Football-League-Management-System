# Generated by Django 5.0.6 on 2024-06-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('PLAYERID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('PLAYERNAME', models.CharField(max_length=30)),
                ('BIRTHDAY', models.DateField()),
                ('NATIONALITY', models.CharField(max_length=20)),
                ('CLUB', models.CharField(max_length=30)),
                ('IMAGE', models.ImageField(upload_to='images/')),
                ('CARDS', models.CharField(default='', max_length=6)),
            ],
        ),
    ]
