# Generated by Django 2.2.10 on 2020-03-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0064_company_pec'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='sdi_code',
            field=models.CharField(blank=True, max_length=7, verbose_name='SDI code'),
        ),
    ]
