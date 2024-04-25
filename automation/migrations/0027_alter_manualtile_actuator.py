# Generated by Django 4.0.1 on 2022-09-10 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_alter_actuator_previous_value_and_more'),
        ('automation', '0026_alter_automatictile_title_alter_manualtile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualtile',
            name='actuator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device.actuator', unique=True),
        ),
    ]