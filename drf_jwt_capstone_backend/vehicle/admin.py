from django.contrib import admin

from .models import Fuel_Type, Vehicle, Vehicle_Type

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Vehicle_Type)
admin.site.register(Fuel_Type)