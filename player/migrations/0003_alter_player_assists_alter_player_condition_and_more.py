# Generated by Django 4.2.13 on 2024-06-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_assists_player_condition_player_goals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ASSISTS',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='CONDITION',
            field=models.CharField(default='Tốt', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='GOALS',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='POSITION',
            field=models.CharField(choices=[('GK', 'Thủ môn'), ('DF', 'Hậu vệ'), ('MF', 'Tiền vệ'), ('FW', 'Tiền đạo')], default='GK', max_length=2),
        ),
        migrations.AlterField(
            model_name='player',
            name='PREFERFOOT',
            field=models.CharField(choices=[('L', 'Chân trái'), ('R', 'Chân phải'), ('B', 'Cả hai chân')], default='R', max_length=1),
        ),
    ]
