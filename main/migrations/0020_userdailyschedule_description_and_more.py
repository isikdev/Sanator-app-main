# Generated by Django 4.2 on 2023-06-20 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_userdailyschedule_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdailyschedule',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdailyschedule',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AddField(
            model_name='userdailyschedule',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='userdailyschedule',
            name='schedule',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userdailyschedule',
            name='weekday',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=9),
        ),
    ]
