# Generated by Django 4.2.2 on 2023-07-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_delete_user_building_building_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invigilator",
            name="Invigilator_phone_number",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
