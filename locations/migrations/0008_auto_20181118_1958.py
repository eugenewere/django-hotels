# Generated by Django 2.1.3 on 2018-11-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_country_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='language1',
        ),
        migrations.RemoveField(
            model_name='country',
            name='language2',
        ),
    ]
