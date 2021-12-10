
from .models import Fuel_Type, OrderItem, ShippingAddress, Vehicle, Vehicle_Type, Order
from typing import OrderedDict
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()


# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Vehicle_Type)
admin.site.register(Fuel_Type)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(User)
