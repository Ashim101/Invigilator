# Generated by Django 4.2.3 on 2023-08-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0016_alter_building_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invigilator",
            name="phone_number",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]