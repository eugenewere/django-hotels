# Generated by Django 2.1.3 on 2018-11-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20181125_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSection',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'website_admin_sections',
                'ordering': ['name'],
            },
        ),
    ]