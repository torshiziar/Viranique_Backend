# Generated by Django 4.0.1 on 2023-01-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0037_alter_manualtile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatictile',
            name='output',
            field=models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF'), ('SWITCH', 'SWITCH')], default='ON', max_length=8),
        ),
    ]