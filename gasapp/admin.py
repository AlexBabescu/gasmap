from django.contrib import admin

from .models import Brands, Stations, FuelTypes, FuelPrices

admin.site.register(Brands)
admin.site.register(Stations)
admin.site.register(FuelTypes)
admin.site.register(FuelPrices)
