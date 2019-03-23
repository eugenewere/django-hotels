# Generated by Django 2.1.5 on 2019-02-08 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0056_servicetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='hotels.ServiceType'),
        ),
    ]