# Generated by Django 2.1.4 on 2018-12-09 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0039_deletion_protect'),
        ('work', '0006_contracttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('roll_number', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('level', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('associated', models.BooleanField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotels.Company')),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.ContractType')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Employee')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.JobType')),
            ],
            options={
                'db_table': 'work_contract',
                'ordering': ['company', 'employee', 'end_date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='contract',
            unique_together={('company', 'employee', 'roll_number'), ('company', 'employee', 'start_date', 'end_date')},
        ),
    ]
