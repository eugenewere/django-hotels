# Generated by Django 2.2.9 on 2020-02-23 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0060_translations'),
        ('work', '0038_timestamp_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='default_structure',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='hotels.Structure', verbose_name='default structure'),
        ),
    ]
