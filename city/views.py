from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.gis.geos import Point
from rest_framework.utils import json

from .models import *
from django.contrib.gis.db.models import Q



def home(request):
    context = {
        "forts": Fort.objects.all(),
        "hospitals": Hospital.objects.all(),
        "markets": Market.objects.all(),
        "polices": PoliceStation.objects.all(),
        "restaurants": Restaurant.objects.all(),
    }
    return render(request, 'index.html', context)


# ---------------------------- Listing Page --------------------------


def list(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            restaurants = Restaurant.objects.filter(
                Q(restaurant__icontains=search) |
                Q(rating__icontains=search) |
                Q(type__startswith=search) |
                Q(features__icontains=search)
            )
            marker_list = []

            for instance in restaurants:
                name = str(instance.restaurant)
                latitude = float(instance.latitude)
                longitude = float(instance.longitude)
                marker_list += [[name, latitude, longitude]]
            if restaurants:
                context = {
                    'marker_list': json.dumps(marker_list),
                    'restaurents': restaurants,
                }
                return render(request, 'listing/restaurant.html', context)

            hospitals = Hospital.objects.filter(
                Q(hospital_n__icontains=search) |
                #Q(hospital_n__endswith=search) |
                Q(hospital_r__icontains=search) |
                Q(contact_nu__startswith=search) |
                Q(address__icontains=search)
            )
            marker_list = []

            for instance in hospitals:
                name = str(instance.hospital_n)
                latitude = float(instance.latitude)
                longitude = float(instance.longitude)
                marker_list += [[name, latitude, longitude]]
            if hospitals:
                context = {
                    'marker_list': json.dumps(marker_list),
                    'hospitals': hospitals,
                }
                return render(request, 'listing/hospital.html', context)

            markets = Market.objects.filter(
                Q(market_nam__icontains=search) |
                Q(rating__icontains=search) |
                Q(location__startswith=search) |
                Q(longitude__icontains=search)
            )
            marker_list = []

            for instance in markets:
                name = str(instance.market_nam)
                latitude = float(instance.latitude)
                longitude = float(instance.longitude)
                marker_list += [[name, latitude, longitude]]
            if markets:
                context = {
                    'marker_list': json.dumps(marker_list),
                    'markets': markets,
                }
                return render(request, 'listing/markets.html', context)

            polices = PoliceStation.objects.filter(
                Q(police_sta__icontains=search) |
                Q(rating__icontains=search) |
                Q(contact_nu__startswith=search) |
                Q(latitude__icontains=search)
            )
            marker_list = []

            for instance in polices:
                name = str(instance.police_sta)
                latitude = float(instance.latitude)
                longitude = float(instance.longitude)
                marker_list += [[name, latitude, longitude]]
            if polices:
                context = {
                    'marker_list': json.dumps(marker_list),
                    'polices': polices,
                }
                return render(request, 'listing/police.html', context)

            forts = Fort.objects.filter(
                Q(title__icontains=search) |
                Q(rating__icontains=search) |
                Q(category__startswith=search) |
                Q(descriptio__icontains=search)
            )
            marker_list = []

            for instance in forts:
                name = str(instance.title)
                latitude = float(instance.latitude)
                longitude = float(instance.longitude)
                marker_list += [[name, latitude, longitude]]
            if forts:
                context = {
                    'marker_list': json.dumps(marker_list),
                    'forts': forts,
                }
                return render(request, 'listing/fort.html', context)
            else:
                return render(request, 'success_or_not/searching_not_found.html')
        else:
            return HttpResponseRedirect('/')

    args = {
        "users": Fort.objects.all(),
    }
    return render(request, 'listing.html', args)


# ---------------------------- Dstails Page --------------------------

def restaurant_details(request, details_id):
    context = {
        'restaurents_id': Restaurant.objects.get(id=details_id),
    }
    return render(request, 'details/restaurant.html', context)


def police_details(request, police_details_id):
    context = {
        'polices_id': PoliceStation.objects.get(id=police_details_id),
    }
    return render(request, 'details/police.html', context)


def market_details(request, market_details_id):
    context = {
        'market_id': Market.objects.get(id=market_details_id),
    }
    return render(request, 'details/market.html', context)


def hospital_details(request, hospital_details_id):
    context = {
        'hospital_id': Hospital.objects.get(id=hospital_details_id),
    }
    return render(request, 'details/hospital.html', context)


def fort_details(request, fort_details_id):
    context = {
        'fort_id': Fort.objects.get(id=fort_details_id),
    }
    return render(request, 'details/fort.html', context)



# --------------------- Single Model Template ---------------



def hospital(request):
    hospitals = Hospital.objects.all()
    return render(request, 'all/hospitals.html', {"hospitals": hospitals})


def markets(request):
    markets = Market.objects.all()
    return render(request, 'all/markets.html', {"markets": markets})


def forts(request):
    forts = Fort.objects.all()
    return render(request, 'all/markets.html', {"forts": forts})


