# Generated by Django 4.0.1 on 2023-01-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0013_sensor_is_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='part_number',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='part_number',
            field=models.CharField(max_length=16),
        ),
    ]
