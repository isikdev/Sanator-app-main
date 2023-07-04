# Generated by Django 4.2 on 2023-06-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_userdailyschedule_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdailyschedule',
            name='weekday',
            field=models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота'), ('Воскресенье', 'Воскресенье')], max_length=11),
        ),
    ]