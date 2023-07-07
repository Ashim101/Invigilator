# Generated by Django 4.2.2 on 2023-07-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['building_name__building_name']},
        ),
        migrations.AddField(
            model_name='room',
            name='isOccupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('building_name', 'room_number')},
        ),
    ]
