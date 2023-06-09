# Generated by Django 4.2 on 2023-04-16 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("characters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Flaw",
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
                    "name",
                    models.CharField(default="New flaw", max_length=255, unique=True),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="skill",
            name="default_attribute",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="characters.attribute",
            ),
        ),
        migrations.CreateModel(
            name="FlawDescription",
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
                    "intensity",
                    models.CharField(
                        choices=[("FIRST", "I"), ("SECOND", "II"), ("THIRD", "III")],
                        default="I",
                        max_length=6,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "flaw",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="characters.flaw",
                    ),
                ),
            ],
        ),
    ]
