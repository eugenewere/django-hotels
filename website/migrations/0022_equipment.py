# Generated by Django 2.1.5 on 2019-01-15 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_removed_roomservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsearchable',
            name='model',
            field=models.CharField(choices=[('ActivityAdmin', 'ActivityAdmin'), ('ActivityInLinesAdmin', 'ActivityInLinesAdmin'), ('ActivityRoomAdmin', 'ActivityRoomAdmin'), ('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('ContractAdmin', 'ContractAdmin'), ('ContractTypeAdmin', 'ContractTypeAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('EquipmentAdmin', 'EquipmentAdmin'), ('JobTypeAdmin', 'JobTypeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('LoginAdmin', 'LoginAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('ServiceAdmin', 'ServiceAdmin'), ('StructureAdmin', 'StructureAdmin'), ('TabletAdmin', 'TabletAdmin'), ('TimestampAdmin', 'TimestampAdmin')], max_length=255),
        ),
        migrations.AlterField(
            model_name='adminsearchable',
            name='ref_model',
            field=models.CharField(choices=[('ActivityAdmin', 'ActivityAdmin'), ('ActivityInLinesAdmin', 'ActivityInLinesAdmin'), ('ActivityRoomAdmin', 'ActivityRoomAdmin'), ('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('ContractAdmin', 'ContractAdmin'), ('ContractTypeAdmin', 'ContractTypeAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('EquipmentAdmin', 'EquipmentAdmin'), ('JobTypeAdmin', 'JobTypeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('LoginAdmin', 'LoginAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('ServiceAdmin', 'ServiceAdmin'), ('StructureAdmin', 'StructureAdmin'), ('TabletAdmin', 'TabletAdmin'), ('TimestampAdmin', 'TimestampAdmin')], max_length=255),
        ),
    ]
