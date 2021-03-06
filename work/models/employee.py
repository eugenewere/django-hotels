##
#     Project: Django Hotels
# Description: A Django application to organize Hotels and Inns
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2020 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import csv
import io
import os.path

from django.db import models
from django.conf import settings
from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import path
from django.utils.safestring import mark_safe
from django.utils.translation import pgettext_lazy

import codicefiscale

import work.models

from locations.models import Country, Location

from utility.admin import AdminTextInputFilter
from utility.admin_widgets import AdminImageWidget_128x128
from utility.forms import CSVImportForm
from utility.misc import reverse_with_query
from utility.models import BaseModel, BaseModelAdmin


class Employee(BaseModel):
    first_name = models.CharField(max_length=255,
                                  verbose_name=pgettext_lazy('Employee',
                                                             'first name'))
    last_name = models.CharField(max_length=255,
                                 verbose_name=pgettext_lazy('Employee',
                                                            'last name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy('Employee',
                                                              'description'))
    gender = models.CharField(max_length=10,
                              default='unknown',
                              choices=(('male', pgettext_lazy('Employee',
                                                              'Male')),
                                       ('female', pgettext_lazy('Employee',
                                                                'Female')),
                                       ('unknown', pgettext_lazy('Employee',
                                                                 'Unknown'))),
                              verbose_name=pgettext_lazy('Employee',
                                                         'gender'))
    birth_date = models.DateField(verbose_name=pgettext_lazy('Employee',
                                                             'birth date'))
    birth_location = models.ForeignKey('locations.Location',
                                       on_delete=models.PROTECT,
                                       default=0,
                                       related_name='employee_birth_location',
                                       verbose_name=pgettext_lazy(
                                           'Employee',
                                           'birth location'))
    address = models.TextField(blank=True,
                               verbose_name=pgettext_lazy('Employee',
                                                          'address'))
    location = models.ForeignKey('locations.Location',
                                 on_delete=models.PROTECT,
                                 default=0,
                                 related_name='employee_location',
                                 verbose_name=pgettext_lazy('Employee',
                                                            'location'))
    postal_code = models.CharField(max_length=15,
                                   blank=True,
                                   verbose_name=pgettext_lazy('Employee',
                                                              'postal code'))
    phone1 = models.CharField(max_length=255,
                              blank=True,
                              verbose_name=pgettext_lazy('Employee',
                                                         'phone 1'))
    phone2 = models.CharField(max_length=255,
                              blank=True,
                              verbose_name=pgettext_lazy('Employee',
                                                         'phone 2'))
    email = models.CharField(max_length=255,
                             blank=True,
                             verbose_name=pgettext_lazy('Employee',
                                                        'email'))
    vat_number = models.CharField(max_length=255,
                                  blank=True,
                                  verbose_name=pgettext_lazy('Employee',
                                                             'VAT number'))
    tax_code = models.CharField(max_length=255,
                                verbose_name=pgettext_lazy('Employee',
                                                           'tax code'))
    bank_account = models.CharField(max_length=255,
                                    blank=True,
                                    verbose_name=pgettext_lazy('Employee',
                                                               'bank account'))
    permit = models.CharField(max_length=255,
                              blank=True,
                              verbose_name=pgettext_lazy('Employee',
                                                         'permit'))
    permit_location = models.ForeignKey('locations.Location',
                                        on_delete=models.PROTECT,
                                        default=0,
                                        blank=True,
                                        null=True,
                                        verbose_name=pgettext_lazy(
                                            'Employee',
                                            'permit location'))
    permit_date = models.DateField(blank=True,
                                   null=True,
                                   default=None,
                                   verbose_name=pgettext_lazy('Employee',
                                                              'permit date'))
    permit_expiration = models.DateField(blank=True,
                                         null=True,
                                         default=None,
                                         verbose_name=pgettext_lazy(
                                             'Employee',
                                             'permit expiration'))
    photo = models.ImageField(null=True,
                              blank=True,
                              upload_to='hotels/images/employees/',
                              default='standard:gender_unknown_1',
                              verbose_name=pgettext_lazy('Employee',
                                                         'photo'))
    locked = models.BooleanField(default=False,
                                 verbose_name=pgettext_lazy('Employee',
                                                            'locked'))

    class Meta:
        # Define the database table
        db_table = 'work_employees'
        ordering = ['first_name', 'last_name']
        unique_together = ('first_name', 'last_name', 'tax_code')
        verbose_name = pgettext_lazy('Employee', 'Employee')
        verbose_name_plural = pgettext_lazy('Employee', 'Employees')

    def __str__(self):
        return '{FIRST_NAME} {LAST_NAME}'.format(
            FIRST_NAME=self.first_name,
            LAST_NAME=self.last_name)

    def clean(self):
        """Validate model fields"""
        # Check tax code field
        tax_code = self.tax_code.upper().strip().ljust(16)
        if not codicefiscale.isvalid(tax_code):
            # Invalid tax code
            raise ValidationError({'tax_code': pgettext_lazy(
                'Employee',
                'Invalid Tax Code')})
        elif codicefiscale.control_code(tax_code[:15]) != tax_code[15]:
            # Unmatching check digit
            raise ValidationError({'tax_code': pgettext_lazy(
                'Employee',
                'Incorrect Tax Code')})
        elif Employee.objects.filter(tax_code=tax_code).exclude(
                pk=self.id):
            # Existing tax code
            raise ValidationError({'tax_code': pgettext_lazy(
                'Employee',
                'Existing Tax Code')})
        else:
            # No errors
            self.tax_code = tax_code

    def get_active_contracts(self, employee_id):
        return work.models.Contract.objects.filter(
            # Active contracts
            work.models.Contract.objects.get_active_contracts_query(),
            # Current employee
            employee=employee_id
        )

    def get_active_contract(self):
        contracts = self.get_active_contracts(self.pk)
        return contracts[0] if contracts else None


class EmployeeFirstNameInputFilter(AdminTextInputFilter):
    parameter_name = 'first_name'
    title = pgettext_lazy('Employee', 'first name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(first_name__icontains=self.value())


class EmployeeLastNameInputFilter(AdminTextInputFilter):
    parameter_name = 'last_name'
    title = pgettext_lazy('Employee', 'last name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(last_name__icontains=self.value())


class EmployeeTaxCodeInputFilter(AdminTextInputFilter):
    parameter_name = 'tax_code'
    title = pgettext_lazy('Employee', 'tax code')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tax_code__icontains=self.value())


class EmployeeBirthLocationCountryFilter(admin.SimpleListFilter):
    parameter_name = 'birth_location'
    title = pgettext_lazy('Employee', 'Birth Location')

    def lookups(self, request, model_admin):
        return Country.objects.all().values_list('name', 'name')

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                birth_location__region__country=self.value())


class EmployeeStatusFilter(admin.SimpleListFilter):
    parameter_name = 'status'
    title = pgettext_lazy('Employee', 'status')

    def lookups(self, request, model_admin):
        return (0, pgettext_lazy('Employee', 'Unlocked')),\
               (1, pgettext_lazy('Employee', 'Locked'))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                locked=self.value())


class EmployeeAdmin(BaseModelAdmin):
    change_list_template = 'utility/import_csv/change_list.html'
    readonly_fields = ('id', 'standard_photos')
    radio_fields = {'gender': admin.HORIZONTAL}

    def save_model(self, request, obj, form, change):
        if not obj.photo or str(obj.photo).startswith('standard:'):
            iconset = 'standard:{ICONSET}'
            obj.photo = iconset.format(ICONSET=request.POST['standard_image'])
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Add subquery for active contract
        contracts = self.model.get_active_contracts(None,
                                                    models.OuterRef('pk'))
        # Add annotated fields for contract id and company
        queryset = queryset.annotate(
            _country=models.F('birth_location__region__country'),
            _contract_id=models.Subquery(contracts.values('pk')[:1]),
            _contract_company=models.Subquery(
                contracts.values('company__name')[:1]),
        )
        return queryset

    def get_urls(self):
        urls = [
            path('import/', self.import_csv),
        ] + super().get_urls()
        return urls

    def import_csv(self, request):
        def append_error(type_name, item):
            """Append an error message to the messages list"""
            error_message = pgettext_lazy('Employee',
                                          'Unexpected {TYPE} "{ITEM}"').format(
                                              TYPE=type_name,
                                              ITEM=item)
            if error_message not in error_messages:
                error_messages.append(error_message)
                self.message_user(request, error_message, messages.ERROR)

        if request.method == 'POST':
            # Preload locations
            locations = {}
            for item in Location.objects.all():
                locations[str(item)] = item
            # Load CSV file content
            csv_file = io.TextIOWrapper(
                request.FILES['csv_file'].file,
                encoding=request.POST['encoding'])
            reader = csv.DictReader(
                csv_file,
                delimiter=request.POST['delimiter'])
            # Load data from CSV
            error_messages = []
            employees = []
            for row in reader:
                if row['BIRTH LOCATION'] not in locations:
                    append_error('location', row['BIRTH LOCATION'])
                elif row['LOCATION'] not in locations:
                    append_error('location', row['LOCATION'])
                elif row['PERMIT LOCATION'] not in locations:
                    append_error('location', row['PERMIT LOCATION'])
                else:
                    # If no error create a new Employee object
                    employees.append(Employee(first_name=row['FIRST NAME'],
                                              last_name=row['LAST NAME'],
                                              description=row['DESCRIPTION'],
                                              gender=row['GENDER'],
                                              birth_date=(row['BIRTH DATE']
                                                          if row['BIRTH DATE']
                                                          else None),
                                              birth_location=locations[
                                                  row['BIRTH LOCATION']],
                                              address=row['ADDRESS'],
                                              location=locations[
                                                  row['LOCATION']],
                                              postal_code=row['POSTAL CODE'],
                                              phone1=row['PHONE1'],
                                              phone2=row['PHONE2'],
                                              email=row['EMAIL'],
                                              vat_number=row['VAT NUMBER'],
                                              tax_code=row['TAX CODE'],
                                              permit=row['PERMIT'],
                                              permit_location=locations[
                                                  row['PERMIT LOCATION']],
                                              permit_date=(
                                                  row['PERMIT DATE']
                                                  if row['PERMIT DATE']
                                                  else None),
                                              permit_expiration=(
                                                  row['PERMIT EXPIRATION']
                                                  if row['PERMIT EXPIRATION']
                                                  else None)))
            # Save data only if there were not errors
            if not error_messages:
                Employee.objects.bulk_create(employees)
                self.message_user(request, pgettext_lazy(
                    'Employee',
                    'Your CSV file has been imported'))
            return redirect('..')
        return render(request,
                      'utility/import_csv/form.html',
                      {'form': CSVImportForm()})

    def detail_photo_image(self, instance, width, height):
        if instance.photo.url.startswith(
                os.path.join(settings.MEDIA_URL, 'standard%3A')):
            iconset = instance.photo.url.split('%3A', 1)[1]
            base_url = os.path.join(settings.STATIC_URL,
                                    'hotels/images/{ICONSET}/'
                                    '{SIZE}x{SIZE}.png')
            url_thumbnail = base_url.format(ICONSET=iconset, SIZE=width)
            url_image = base_url.format(ICONSET=iconset, SIZE=512)
        else:
            # Show image
            url_thumbnail = instance.photo.url
            url_image = url_thumbnail

        return mark_safe('<a href="{url}" target="_blank">'
                         '<img src="{thumbnail}" '
                         'width="{width}" '
                         'height={height} />'.format(url=url_image,
                                                     thumbnail=url_thumbnail,
                                                     width=width,
                                                     height=height))

    def photo_image(self, instance):
        return self.detail_photo_image(instance, 128, 128)
    photo_image.short_description = pgettext_lazy('Employee', 'Photo image')

    def photo_thumbnail(self, instance):
        return self.detail_photo_image(instance, 48, 48)
    photo_thumbnail.short_description = pgettext_lazy('Employee',
                                                      'Photo thumbnail')

    def formfield_for_dbfield(self, db_field, **kwargs):
        # For ImageField fields replace the rendering widget
        if isinstance(db_field, models.ImageField):
            kwargs['widget'] = AdminImageWidget_128x128
            # Remove request argument
            kwargs.pop('request', None)
            return db_field.formfield(**kwargs)
        else:
            return super().formfield_for_dbfield(db_field, **kwargs)

    def get_fields(self, request, obj=None):
        """Reorder the fields list"""
        fields = super().get_fields(request, obj)
        fields = ['id'] + [k for k in fields if k not in 'id']
        return fields

    def standard_photos(self, instance):
        template = loader.get_template('hotels/employee_standard_photos.html')
        context = {
            'photo': str(instance.photo).replace('standard:', ''),
            'iconsets': ('gender_unknown_1',
                         'gender_female_1',
                         'gender_female_2',
                         'gender_female_3',
                         'gender_female_4',
                         'gender_male_1',
                         'gender_male_2',
                         'gender_male_3',
                         'gender_male_4',
                         'gender_male_5',
                         'gender_male_6',
                         'gender_male_7')
        }
        return template.render(context)
    standard_photos.short_description = pgettext_lazy('Employee',
                                                      'Standard photos')

    # noinspection PyProtectedMember
    def active_contract(self, instance):
        if instance._contract_id:
            link = reverse_with_query(view='admin:work_contract_change',
                                      args=[instance._contract_id])
            link_classes = ''
            link_text = instance._contract_company
        else:
            link = reverse_with_query(view='admin:work_contract_add',
                                      query={'employee': instance.pk})
            link_classes = 'addlink'
            link_text = pgettext_lazy('Employee', 'Add')
        return mark_safe('<a href="{LINK}" {CLASSES}>{TEXT}</a>'.format(
            LINK=link,
            CLASSES='class="{CLASSES}"'.format(CLASSES=link_classes)
                    if link_classes else '',
            TEXT=link_text))
    active_contract.short_description = pgettext_lazy('Employee',
                                                      'Active contract')

    def country(self, instance):
        # noinspection PyProtectedMember
        return instance._country
    country.short_description = pgettext_lazy('Employee', 'Country')

    def status(self, instance):
        """Invert the locked status for display purposes"""
        return not instance.locked
    status.boolean = True
