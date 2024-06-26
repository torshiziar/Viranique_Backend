# Generated by Django 4.0.1 on 2022-08-25 05:01

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0005_actuator_set_time_actuator_set_timeout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='set_time',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='set_value'),
        ),
    ]
