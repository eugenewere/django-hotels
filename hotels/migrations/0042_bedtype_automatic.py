# Generated by Django 2.1.4 on 2019-01-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0041_roomservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedtype',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bedtype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
