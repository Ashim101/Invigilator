# Generated by Django 4.2.3 on 2023-08-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0017_alter_invigilator_phone_number"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="examhallsession",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="exam",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="exam",
            name="start_time",
        ),
        migrations.AlterField(
            model_name="exam",
            name="shift",
            field=models.CharField(
                choices=[("6-9", "6-9"), ("12-12", "10-12")],
                default="6-9",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="examhallsession",
            name="shift",
            field=models.CharField(
                choices=[("Morning", "Morning"), ("Day", "Day")],
                default="Morning",
                max_length=255,
            ),
        ),
    ]
