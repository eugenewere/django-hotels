# Generated by Django 2.1.3 on 2018-11-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_regions_aliases'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='aliases',
            field=models.ManyToManyField(db_table='locations_region_aliases', to='locations.RegionAlias'),
        ),
    ]