# Generated by Django 4.2 on 2023-06-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_delete_procbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posters',
            old_name='opisanie',
            new_name='description',
        ),
        migrations.AddField(
            model_name='posters',
            name='image',
            field=models.ImageField(default='default.png', upload_to='posters/', verbose_name='Изображение'),
        ),
    ]
