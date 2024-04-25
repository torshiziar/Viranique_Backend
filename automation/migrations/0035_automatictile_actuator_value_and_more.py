# Generated by Django 4.0.1 on 2022-11-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0034_remove_manualtile_unique_manual_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='automatictile',
            name='actuator_value',
            field=models.FloatField(blank=True, choices=[(0.0, 'off'), (1.0, 'on')], null=True),
        ),
        migrations.AddField(
            model_name='manualtile',
            name='actuator_value',
            field=models.FloatField(blank=True, choices=[(0.0, 'off'), (1.0, 'on')], null=True),
        ),
    ]