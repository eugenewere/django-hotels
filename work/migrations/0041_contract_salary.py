# Generated by Django 2.2.10 on 2020-03-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0040_drop_work_activities_full_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='montly salary'),
        ),
    ]
