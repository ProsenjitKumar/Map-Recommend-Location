from django.contrib.gis import admin
from .models import *


class RestaurantAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['restaurant', 'type', 'cost', 'address']
    search_fields = ['restaurant', 'type', 'cost', 'address']


admin.site.register(Restaurant, RestaurantAdmin)


class FortAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['title']
    search_fields = ['title', 'category', 'descriptio']


admin.site.register(Fort, FortAdmin)


class HospitalAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['hospital_n']
    search_fields = ['hospital_n']


admin.site.register(Hospital, HospitalAdmin)


class MarketAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['market_nam']
    search_fields = ['market_nam', 'location', 'rating']


admin.site.register(Market, MarketAdmin)


class PoliceStationAdmin(admin.OSMGeoAdmin):
    list_per_page = 25
    list_filter = ['police_sta']
    search_fields = ['police_sta', 'address', 'rating', 'contact_nu']


admin.site.register(PoliceStation, PoliceStationAdmin)
