# Generated by Django 4.2.3 on 2023-07-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_alter_invigilator_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invigilator",
            name="post",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="invigilator",
            name="age",
            field=models.IntegerField(),
        ),
    ]