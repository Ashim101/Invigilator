# Generated by Django 4.2.3 on 2023-08-03 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0020_remove_exam_shift_exam_shift"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="regular_or_back",
            field=models.CharField(
                choices=[("Regular", "Regular"), ("Back", "Back"), ("None", "None")],
                default="Regular",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="exam",
            name="semester_type",
            field=models.CharField(
                choices=[("Odd", "odd"), ("Even", "Even"), ("None", "None")],
                default="Odd",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="examhallsession",
            name="shift",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="examhallsessions",
                to="home.shift",
            ),
        ),
    ]
