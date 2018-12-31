from django.contrib.gis.db import models


class Restaurant(models.Model):
    restaurant = models.CharField(max_length=254)
    rating = models.FloatField()
    type = models.CharField(max_length=254)
    cuisines = models.CharField(max_length=254)
    cost = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    features = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant


class Fort(models.Model):
    title = models.CharField(max_length=254)
    rating = models.FloatField()
    category = models.CharField(max_length=254)
    descriptio = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.PointField()

    def __str__(self):
        return self.title


class Hospital(models.Model):
    hospital_n = models.CharField(max_length=255)
    hospital_r = models.FloatField()
    contact_nu = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField()

    def __str__(self):
        return self.hospital_n



class Market(models.Model):
    market_nam = models.CharField(max_length=255)
    rating = models.FloatField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField()

    def __str__(self):
        return self.market_nam


class PoliceStation(models.Model):
    police_sta = models.CharField(max_length=255)
    rating = models.FloatField()
    contact_nu = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField()

    def __str__(self):
        return self.police_sta
