# Generated by Django 4.2 on 2023-05-06 08:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mythic", "0011_list_sceneadjustmenttable_listnote_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SceneAdjustmentTable",
            new_name="SceneAdjustmentOption",
        ),
    ]
