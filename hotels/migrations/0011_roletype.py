# Generated by Django 2.1.3 on 2018-11-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0010_auto_20181111_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'roletypes',
            },
        ),
    ]
