# Generated by Django 4.2.3 on 2023-08-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0021_alter_exam_regular_or_back_alter_exam_semester_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invigilator",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female"), ("Others", "Others")],
                default="Male",
                max_length=7,
            ),
        ),
    ]