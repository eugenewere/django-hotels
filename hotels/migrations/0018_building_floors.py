# Generated by Django 2.1.3 on 2018-11-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0017_building_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='floors',
            field=models.PositiveIntegerField(),
        ),
    ]
