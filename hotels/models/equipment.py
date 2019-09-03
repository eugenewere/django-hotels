##
#     Project: Django Hotels
# Description: A Django application to organize Hotels and Inns
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2019 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

from django.db import models
from django.utils.translation import pgettext_lazy

from utility.models import BaseModel, BaseModelAdmin


class Equipment(BaseModel):
    structure = models.ForeignKey('Structure',
                                  on_delete=models.PROTECT,
                                  default=0,
                                  verbose_name=pgettext_lazy('Equipment',
                                                             'structure'))
    name = models.CharField(max_length=255,
                            verbose_name=pgettext_lazy('Equipment',
                                                       'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy('Equipment',
                                                              'description'))
    equipment_type = models.ForeignKey('EquipmentType',
                                       on_delete=models.PROTECT,
                                       default=0,
                                       verbose_name=pgettext_lazy(
                                           'Equipment', 'equipment type'))
    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name=pgettext_lazy(
                                               'Equipment',
                                               'quantity'))

    class Meta:
        # Define the database table
        db_table = 'hotels_equipments'
        ordering = ['structure', 'name']
        unique_together = ('structure', 'name')
        verbose_name = pgettext_lazy('Equipment', 'Equipment')
        verbose_name_plural = pgettext_lazy('Equipment', 'Equipments')

    def __str__(self):
        return self.name


class EquipmentAdmin(BaseModelAdmin):
    pass
