# Generated by Django 4.2.3 on 2023-07-10 23:09

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_alter_examhallsession_shift"),
    ]

    operations = [
        migrations.AddField(
            model_name="building",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="exam",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="examhallsession",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="date",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="invigilator",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="firstname",
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="room",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="room_number",
                unique=True,
            ),
        ),
    ]
