# Generated by Django 4.0.1 on 2023-01-06 12:35

import authentication.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_alter_user_email_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=authentication.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'gif', 'jpg'])]),
        ),
    ]
