# Generated by Django 2.1.5 on 2019-04-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0057_service_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='show_in_app',
            field=models.BooleanField(default=False),
        ),
    ]
