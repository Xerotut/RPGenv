# Generated by Django 4.2 on 2023-05-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mythic", "0019_game_time_created_listnote_time_created_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="scene",
            constraint=models.UniqueConstraint(
                fields=("name", "game"), name="unique_scene_in_game"
            ),
        ),
    ]
