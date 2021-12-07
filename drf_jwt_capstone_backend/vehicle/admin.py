from typing import OrderedDict
from django.contrib import admin

from .models import Fuel_Type, OrderItem, ShippingAddress, Vehicle, Vehicle_Type, Order

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Vehicle_Type)
admin.site.register(Fuel_Type)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
