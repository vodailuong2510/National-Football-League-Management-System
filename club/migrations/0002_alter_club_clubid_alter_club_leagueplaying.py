from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='CLUBID',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='club',
            name='LEAGUEPLAYING',
            field=models.CharField(max_length=100),
        ),
    ]