# Generated by Django 2.1.5 on 2019-02-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_admin_list_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminsearchable',
            name='model',
            field=models.CharField(choices=[('ActivityAdmin', 'ActivityAdmin'), ('ActivityInLinesAdmin', 'ActivityInLinesAdmin'), ('ActivityRoomAdmin', 'ActivityRoomAdmin'), ('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminSectionAdmin', 'AdminSectionAdmin'), ('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('ContractAdmin', 'ContractAdmin'), ('ContractTypeAdmin', 'ContractTypeAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('EquipmentAdmin', 'EquipmentAdmin'), ('EquipmentTypeAdmin', 'EquipmentTypeAdmin'), ('HomeSectionAdmin', 'HomeSectionAdmin'), ('JobTypeAdmin', 'JobTypeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('LoginAdmin', 'LoginAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('ServiceAdmin', 'ServiceAdmin'), ('ServiceExtraAdmin', 'ServiceExtraAdmin'), ('StructureAdmin', 'StructureAdmin'), ('TabletAdmin', 'TabletAdmin'), ('TimestampAdmin', 'TimestampAdmin'), ('TimestampDirectionAdmin', 'TimestampDirectionAdmin')], max_length=255),
        ),
        migrations.AlterField(
            model_name='adminsearchable',
            name='ref_model',
            field=models.CharField(choices=[('ActivityAdmin', 'ActivityAdmin'), ('ActivityInLinesAdmin', 'ActivityInLinesAdmin'), ('ActivityRoomAdmin', 'ActivityRoomAdmin'), ('AdminListDisplayAdmin', 'AdminListDisplayAdmin'), ('AdminSectionAdmin', 'AdminSectionAdmin'), ('BedTypeAdmin', 'BedTypeAdmin'), ('BrandAdmin', 'BrandAdmin'), ('BuildingAdmin', 'BuildingAdmin'), ('CompanyAdmin', 'CompanyAdmin'), ('ContinentAdmin', 'ContinentAdmin'), ('ContractAdmin', 'ContractAdmin'), ('ContractTypeAdmin', 'ContractTypeAdmin'), ('CountryAdmin', 'CountryAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('EquipmentAdmin', 'EquipmentAdmin'), ('EquipmentTypeAdmin', 'EquipmentTypeAdmin'), ('HomeSectionAdmin', 'HomeSectionAdmin'), ('JobTypeAdmin', 'JobTypeAdmin'), ('LanguageAdmin', 'LanguageAdmin'), ('LocationAdmin', 'LocationAdmin'), ('LoginAdmin', 'LoginAdmin'), ('PositionAdmin', 'PositionAdmin'), ('RegionAdmin', 'RegionAdmin'), ('RegionAliasAdmin', 'RegionAliasAdmin'), ('RoomAdmin', 'RoomAdmin'), ('RoomTypeAdmin', 'RoomTypeAdmin'), ('ServiceAdmin', 'ServiceAdmin'), ('ServiceExtraAdmin', 'ServiceExtraAdmin'), ('StructureAdmin', 'StructureAdmin'), ('TabletAdmin', 'TabletAdmin'), ('TimestampAdmin', 'TimestampAdmin'), ('TimestampDirectionAdmin', 'TimestampDirectionAdmin')], max_length=255),
        ),
    ]
