import os
from django.contrib.gis.utils import LayerMapping
from .models import PoliceStation

world_mapping = {
    #'serial' : 'S.no',
    'police_sta' : 'police_sta',
    'rating' : 'rating',
    'contact_nu' : 'contact_nu',
    'address' : 'address',
    'latitude' : 'latitude',
    'longitude' : 'longitude',
    'point' : 'POINT',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'police', 'police.shp'),
)


def run(verbose=True):
    lm = LayerMapping(PoliceStation, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)