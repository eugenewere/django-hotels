# Generated by Django 2.1.4 on 2018-12-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_adminoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSearchable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('AdminOptionAdmin', 'AdminOptionAdmin'), ('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('StructureAdmin', 'StructureAdmin')], max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('ref_model', models.CharField(choices=[('AdminOptionAdmin', 'AdminOptionAdmin'), ('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('StructureAdmin', 'StructureAdmin')], max_length=255)),
                ('ref_field', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('use_select2', models.BooleanField()),
            ],
            options={
                'db_table': 'website_admin_searchable',
                'ordering': ['model', 'field'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='adminsearchable',
            unique_together={('model', 'field')},
        ),
    ]
