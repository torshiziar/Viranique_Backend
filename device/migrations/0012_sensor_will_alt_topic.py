# Generated by Django 4.0.1 on 2022-12-31 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0011_alter_actuator_organization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='will_alt_topic',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]