# Generated by Django 4.2 on 2023-06-19 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]
