# Generated by Django 4.0.1 on 2022-08-15 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('automation', '0018_alter_automatictile_actuator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatictile',
            name='condition_content_type',
            field=models.ForeignKey(blank=True, limit_choices_to={'model__in': ('continues', 'binary', 'schedule')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]