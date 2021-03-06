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

import datetime
import json

from django.db import models
from django.utils import timezone

from hotels.models import Room
from hotels.models import Service
from hotels.models import ServiceExtra

from jsonapi.models import ApiCommand

from work.models import Contract
from work.models import TimestampDirection

from .api_base import APIv1BaseView


class APIv1GetView(APIv1BaseView):
    login_with_tablet_id = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # List all buildings and structures for the selected tablet
        structures = {}
        buildings_set = set()
        for obj_building in self.tablet.buildings.all():
            obj_structure = obj_building.structure
            if obj_structure.name not in structures:
                # Add new structure if doesn't exist
                obj_location = obj_structure.location
                obj_region = obj_location.region
                obj_country = obj_region.country
                structure = {'structure': {'id': obj_structure.id,
                                           'name': obj_structure.name
                                           },
                             'company': {'id': obj_structure.company.pk,
                                         'name': obj_structure.company.name
                                         },
                             'brand': {'id': obj_structure.brand.pk,
                                       'name': obj_structure.brand.name
                                       },
                             'location': {'id': obj_location.pk,
                                          'name': obj_location.name,
                                          'address': obj_structure.address,
                                          'region': {'id': obj_region.pk,
                                                     'name': obj_region.name
                                                     },
                                          'country': {'id': obj_country.pk,
                                                      'name': obj_country.name
                                                      },
                                          },
                             'buildings': [],
                             'extras': [],
                             'service_extra': [],
                             }
                # Add service extra to structure
                for obj_extra in ServiceExtra.objects.filter(
                        structure_id=obj_structure.id):
                    service_extra = {'id': obj_extra.id,
                                     'service_id': obj_extra.service_id,
                                     'price': float(obj_extra.price)}
                    structure['service_extra'].append(service_extra)
                structures[obj_structure.name] = structure
            # Add buildings to the structure
            structure = structures[obj_building.structure.name]
            buildings = structure['buildings']
            extras = structure['extras']
            obj_location = obj_building.location
            obj_region = obj_location.region
            obj_country = obj_region.country
            rooms = Room.objects.filter(building_id=obj_building.id).values(
                'id', 'name', 'description', 'room_type__name',
                'bed_type__name')
            if rooms:
                building = {'building': {'id': obj_building.id,
                                         'name': obj_building.name,
                                         },
                            'location': {'id': obj_location.pk,
                                         'name': obj_location.name,
                                         'address': obj_structure.address,
                                         'region': {'id': obj_region.pk,
                                                    'name': obj_region.name
                                                    },
                                         'country': {'id': obj_country.pk,
                                                     'name': obj_country.name
                                                     },
                                         },
                            'rooms': [{'room': {'id': room['id'],
                                                'name': room['name']
                                                },
                                       'room_type': room['room_type__name'],
                                       'bed_type': room['bed_type__name'],
                                       }
                                      for room in rooms],
                            }
                if not obj_building.extras:
                    buildings_set.add(obj_building.id)
                    buildings.append(building)
                else:
                    extras.append(building)
        context['structures'] = structures
        # List all the contracts for the selected tablet
        contracts = []
        for obj_contract in Contract.objects.filter(
                # Include only contracts with some buildings
                models.Q(buildings__in=self.tablet.buildings.all()),
                # Include only enabled contracts
                models.Q(enabled=True),
                # Include only started contracts
                models.Q(start_date__lte=datetime.date.today()),
                # Include only not expired contracts
                (models.Q(end_date__isnull=True) |
                 models.Q(end_date__gte=datetime.date.today()))).distinct():
            obj_employee = obj_contract.employee
            obj_contract_type = obj_contract.contract_type
            obj_buildings = obj_contract.buildings
            contract = {'contract': {'id': obj_contract.pk,
                                     'guid': obj_contract.guid,
                                     'start': obj_contract.start_date,
                                     'end': obj_contract.end_date
                                     if obj_contract.end_date is not None
                                     else '2099-12-31',
                                     'enabled': obj_contract.enabled,
                                     'active': obj_contract.active()
                                     },
                        'employee': {'id': obj_employee.pk,
                                     'first_name': obj_employee.first_name,
                                     'last_name': obj_employee.last_name,
                                     'gender': obj_employee.gender
                                     },
                        'company': {'id': obj_contract.company.pk,
                                    'name': obj_contract.company.name
                                    },
                        'type': {'id': obj_contract_type.pk,
                                 'name': obj_contract_type.name,
                                 'daily': obj_contract_type.daily_hours,
                                 'weekly': obj_contract_type.weekly_hours,
                                 },
                        'job': {'id': obj_contract.job_type.pk,
                                'name': obj_contract.job_type.name,
                                },
                        'buildings': [building_id['id']
                                      for building_id
                                      in obj_buildings.values('id')
                                      if building_id['id'] in buildings_set]
                        }
            contracts.append(contract)
        context['contracts'] = contracts
        # Add services
        context['services'] = Service.objects.filter(room_service=True).values(
            'id', 'name', 'extra_service', 'show_in_app')
        # Add timestamp directions
        context['timestamp_directions'] = TimestampDirection.objects.exclude(
            id=0).values('id', 'name', 'description', 'short_code',
                         'type_enter', 'type_exit')
        # Add commands
        commands = []
        for command in ApiCommand.objects.filter(
                # Filter for every tablet or only the selected tablet
                (models.Q(tablets=None) | models.Q(tablets=self.tablet.pk)),
                # Filter for after and before values
                (models.Q(starting=None) |
                    models.Q(starting__lte=timezone.now())),
                (models.Q(ending=None) |
                    models.Q(ending__gte=timezone.now())),
                enabled=True):
            # Prepare Command arguments
            command_arguments = json.loads(command.command_type.command)
            if command.command:
                command_arguments.update(json.loads(command.command))
            commands.append({
                'id': command.id,
                'name': command.name,
                'command_type': '{COMMAND} - '.format(
                        COMMAND=command.command_type.name).split(' -')[0],
                'context': command.context_type.name,
                'uses': command.uses,
                'command': command_arguments
            })
        context['commands'] = commands
        # Add closing status (to check for transmission errors)
        self.add_status(context)
        return context
