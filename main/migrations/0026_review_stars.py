# Generated by Django 4.2 on 2023-06-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_rename_opisanie_posters_description_posters_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
