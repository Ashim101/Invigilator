# Generated by Django 4.2.3 on 2023-07-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_alter_exam_regular_or_back_alter_exam_semester_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examhallsession",
            name="shift",
            field=models.CharField(
                choices=[("Morning", "Morning"), ("Day", "Day")],
                default="Day",
                max_length=255,
            ),
        ),
    ]
