# Generated by Django 4.2 on 2023-05-05 09:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mythic", "0006_randomeventfocus"),
    ]

    operations = [
        migrations.CreateModel(
            name="MeaningTable",
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
                        choices=[
                            ("ACTION", "Action"),
                            ("DESCRIPTION", "Description"),
                            ("ELEMENT", "Element"),
                        ],
                        max_length=155,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MeaningTableElement",
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
                    "d100",
                    models.IntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ("word", models.CharField(verbose_name=100)),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="mythic.meaningtable",
                    ),
                ),
            ],
        ),
    ]
