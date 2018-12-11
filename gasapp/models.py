from django.db import models
from django.utils import timezone


# Create your models here.

# Brand Model
# Deals with the basic information of a Brand for a gas Station
# Brand ID, Brand name

class Brands(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.name,self.active)

    class Meta:
        verbose_name_plural = "brands"


# Station Model
# Stores various information of the station
# Station ID, Station name, Brand ID, address, phone number, coordinates, active

class Stations(models.Model):
    name = models.CharField(max_length=255, null=False)
    #brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=30, null=False)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    active = models.BooleanField(True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.name, self.brand, self.address,
                                                         self.phone_number, self.lat, self.lng, self.active)

    class Meta:
        verbose_name_plural = "stations"


# Fuel type Model
# Records various types of fuels
# Fuel ID, Fuel type

class FuelTypes(models.Model):
    type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "fuel types"

# Fuel price Model
# Records various types of fuels
# Station ID, Fuel Type ID, price, date


class FuelPrices(models.Model):
    price = models.FloatField(null=False)
    station = models.ForeignKey(Stations, on_delete=models.DO_NOTHING)
    fuel_type = models.ForeignKey(FuelTypes, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.price, self.station, self.fuel_type, self.date_added)

    class Meta:
        verbose_name_plural = "fuel prices"

#
# # User Model
# # Stores Usename and Password
# # Fuel ID, Fuel type
#
# class Users(models.Model):
#     email = models.CharField(max_length=255, null=False)
#     password = models.CharField(max_length=255, null=False)
#
#     def __str__(self):
#         return "{} - {}".format(self.email, self.password)
