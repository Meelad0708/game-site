# Generated by Django 3.2 on 2024-02-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_rpg_rpggame_sports_sportsgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpggame',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shootergame',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sportsgame',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
