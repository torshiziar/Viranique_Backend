# Generated by Django 4.0.1 on 2022-09-07 11:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0021_alter_notificationmanager_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmanager',
            name='last_seen',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 11, 54, 17, 222811, tzinfo=utc)),
        ),
    ]