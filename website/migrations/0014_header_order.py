# Generated by Django 2.1.4 on 2018-12-21 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_login_required'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homesection',
            options={'ordering': ['header_order']},
        ),
    ]
