# Generated by Django 2.1.3 on 2018-11-24 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0013_auto_20181119_0150'),
        ('hotels', '0018_building_floors'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='location',
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to='locations.Location'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to='locations.Location'),
        ),
    ]
