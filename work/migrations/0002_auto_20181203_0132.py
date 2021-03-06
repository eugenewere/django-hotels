# Generated by Django 2.1.3 on 2018-12-03 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_employee'),
        ('hotels', '0038_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='employee_birth_location', to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='employee_location', to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permit_location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='locations.Location'),
        ),
    ]
