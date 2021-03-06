# Generated by Django 2.2.5 on 2019-09-03 17:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0034_remove_login_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-date', 'contract__employee'], 'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='activityinlinesproxy',
            options={'verbose_name': 'Activity with Rooms', 'verbose_name_plural': 'Activities with Rooms'},
        ),
        migrations.AlterModelOptions(
            name='activityroom',
            options={'ordering': ['activity', 'room', 'service'], 'verbose_name': 'Activity Room', 'verbose_name_plural': 'Activity Rooms'},
        ),
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['company', 'employee', 'end_date'], 'verbose_name': 'Contract', 'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterModelOptions(
            name='contracttype',
            options={'ordering': ['name'], 'verbose_name': 'Contract type', 'verbose_name_plural': 'Contract types'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='jobtype',
            options={'ordering': ['name'], 'verbose_name': 'Job type', 'verbose_name_plural': 'Job types'},
        ),
        migrations.AlterModelOptions(
            name='login',
            options={'verbose_name': 'Login', 'verbose_name_plural': 'Logins'},
        ),
        migrations.AlterModelOptions(
            name='tablet',
            options={'ordering': ['id'], 'verbose_name': 'Tablet', 'verbose_name_plural': 'Tablets'},
        ),
        migrations.AlterModelOptions(
            name='timestamp',
            options={'ordering': ['contract', 'date', 'time'], 'verbose_name': 'Timestamp', 'verbose_name_plural': 'Timestamps'},
        ),
        migrations.AlterModelOptions(
            name='timestampdirection',
            options={'ordering': ['name'], 'verbose_name': 'Timestamp direction', 'verbose_name_plural': 'Timestamp directions'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Contract', verbose_name='contract'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='activityroom',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Activity', verbose_name='activity'),
        ),
        migrations.AlterField(
            model_name='activityroom',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='activityroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotels.Room', verbose_name='room'),
        ),
        migrations.AlterField(
            model_name='activityroom',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotels.Service', verbose_name='service'),
        ),
        migrations.AlterField(
            model_name='activityroom',
            name='service_qty',
            field=models.PositiveIntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='associated',
            field=models.BooleanField(verbose_name='associated'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='buildings',
            field=models.ManyToManyField(blank=True, db_table='work_contract_buildings', to='hotels.Building', verbose_name='buildings'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotels.Company', verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='work.ContractType', verbose_name='contract type'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Employee', verbose_name='employee'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='guid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='job_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='work.JobType', verbose_name='job type'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='level',
            field=models.PositiveIntegerField(verbose_name='level'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='roll_number',
            field=models.CharField(max_length=255, verbose_name='roll number'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='daily_hours',
            field=models.PositiveIntegerField(verbose_name='daily hours'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='weekly_hours',
            field=models.PositiveIntegerField(verbose_name='weekly hours'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='bank_account',
            field=models.CharField(blank=True, max_length=255, verbose_name='bank account'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(verbose_name='birth date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='employee_birth_location', to='locations.Location', verbose_name='birth location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')], default='unknown', max_length=10, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='employee_location', to='locations.Location', verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permit',
            field=models.CharField(blank=True, max_length=255, verbose_name='permit'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permit_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='permit date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permit_expiration',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='permit expiration'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permit_location',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.Location', verbose_name='permit location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone1',
            field=models.CharField(blank=True, max_length=255, verbose_name='phone 1'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone2',
            field=models.CharField(blank=True, max_length=255, verbose_name='phone 2'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default='standard:gender_unknown_1', null=True, upload_to='hotels/images/employees/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='postal_code',
            field=models.CharField(blank=True, max_length=15, verbose_name='postal code'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tax_code',
            field=models.CharField(max_length=255, verbose_name='tax code'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='vat_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='VAT number'),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='login',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Contract', verbose_name='contract'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='buildings',
            field=models.ManyToManyField(blank=True, db_table='work_tablet_buildings', to='hotels.Building', verbose_name='buildings'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='guid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Contract', verbose_name='contract'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.TimestampDirection', verbose_name='direction'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='time',
            field=models.TimeField(verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='timestampdirection',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='timestampdirection',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='timestampdirection',
            name='short_code',
            field=models.CharField(blank=True, max_length=3, verbose_name='short code'),
        ),
        migrations.AlterField(
            model_name='timestampdirection',
            name='type_enter',
            field=models.BooleanField(verbose_name='type enter'),
        ),
        migrations.AlterField(
            model_name='timestampdirection',
            name='type_exit',
            field=models.BooleanField(verbose_name='type exit'),
        ),
    ]
