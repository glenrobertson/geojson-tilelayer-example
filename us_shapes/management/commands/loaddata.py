from django.core.management.base import BaseCommand
from django.contrib.gis.utils.layermapping import LayerMapping
from us_shapes.models import US_State


class Command(BaseCommand):

    def handle(self, shapefile_path, **kwargs):
        LayerMapping(US_State,
            shapefile_path, {
                'sub_region': 'SUB_REGION',
                'geom': 'POLYGON',
                'state_name': 'STATE_NAME'
            }, source_srs=4326
        ).save(strict=True, verbose=True)
