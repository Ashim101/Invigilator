# Generated by Django 4.2.2 on 2023-07-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_alter_room_options_room_isoccupied_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invigilator",
            name="isAssigned",
            field=models.BooleanField(default=False),
        ),
    ]
