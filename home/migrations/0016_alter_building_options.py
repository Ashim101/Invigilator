# Generated by Django 4.2.3 on 2023-07-30 19:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0015_alter_examhallsession_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="building",
            options={"ordering": ["name"]},
        ),
    ]