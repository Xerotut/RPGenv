# Generated by Django 4.2 on 2023-05-06 08:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mythic", "0010_remove_meaningtableelement_d100_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("CHARACTER", "Character"), ("THREAD", "Thread")],
                        max_length=155,
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mythic.game"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SceneAdjustmentTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "yes_if_equal_or_lower",
                    models.IntegerField(
                        default=1,
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ],
                    ),
                ),
                ("result", models.CharField(max_length=155)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ListNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(blank=True, null=True)),
                (
                    "note_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mythic.list"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="list",
            constraint=models.UniqueConstraint(
                fields=("type", "game"), name="unique_list_in_game"
            ),
        ),
    ]