# Generated by Django 4.0.1 on 2022-08-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_alter_sensor_previous_value_alter_sensor_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='previous_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
