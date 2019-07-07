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

from utility.models import BaseModel, BaseModelAdmin


class HomeSection(BaseModel):

    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=255, blank=True)
    header_title = models.CharField(max_length=255, blank=True)
    header_order = models.IntegerField()
    home_title = models.CharField(max_length=255, blank=True)
    home_order = models.IntegerField()
    home_image = models.CharField(max_length=255, blank=True)
    login_required = models.BooleanField(default=False)
    admin_login_required = models.BooleanField(default=False)

    class Meta:
        # Define the database table
        db_table = 'website_home_sections'
        ordering = ['header_order']

    def __str__(self):
        return self.name


class HomeSectionAdmin(BaseModelAdmin):
    pass
