# Generated by Django 4.2.13 on 2024-06-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_league_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='IMAGE',
            new_name='LOGO',
        ),
        migrations.AlterField(
            model_name='league',
            name='ASSOCIATION',
            field=models.CharField(max_length=50),
        ),
    ]