import os
from django.contrib.gis.utils import LayerMapping
from .models import Fort

world_mapping = {
    #'serial' : 'S.no',
    'title' : 'title',
    'rating' : 'rating',
    'category' : 'category',
    'descriptio' : 'descriptio',
    'latitude' : 'latitude',
    'longitude' : 'longitude',
    'point' : 'POINT',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'fort', 'fort1.shp'),
)


def run(verbose=True):
    lm = LayerMapping(Fort, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
