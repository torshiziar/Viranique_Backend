# Generated by Django 4.0.1 on 2022-09-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0020_automatictile_deleted_at_manualtile_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatictile',
            name='delay',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
