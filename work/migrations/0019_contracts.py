# Generated by Django 2.1.4 on 2019-01-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0018_job_type_automatic'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contract',
            table='work_contracts',
        ),
    ]

    atomic = False

