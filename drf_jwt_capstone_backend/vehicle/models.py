from django.db.models.fields import CharField, DateField
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your Models here.
class Vehicle_Type(models.Model):
    vehicle_type = models.CharField(max_length=15)

    def __str__(self):
        return self.vehicle_type


class Fuel_Type(models.Model):
    fuel_type = models.CharField(max_length=20)

    def __str__(self):
        return self.fuel_type


class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    VIN = models.CharField(max_length=50, blank=True, null=True)
    make = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=30, blank=True, null=True)
    mfr = models.IntegerField(blank=True, null=True)
    millage = models.IntegerField(blank=True, null=True, default=50000)
    color = models.CharField(max_length=20, blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, default='Sedan')
    main_image = models.ImageField(
        upload_to='images', null=True, blank=True, default='/sample.jpg')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    purchased_date = DateField()
    date_sold = DateField(blank=True, null=True)
    fuel_type = models.CharField(
        max_length=20, default='Gas', blank=True, null=True)
    features = models.CharField(max_length=100, blank=True, null=True)
    number_of_doors = models.CharField(
        max_length=20, default='4', blank=True, null=True)
    rowseat = models.IntegerField(blank=True, null=True, default=2)
    transmission = models.CharField(
        max_length=20,  default='Automatic', blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    isSold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.make} {self.model} {self.mfr}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=30, null=True, blank=True)
    dealerFees = models.DecimalField(max_digits=7, decimal_places=2)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)

    isPaid = models.BooleanField(default=False)
    paidAt = models.DateField(
        auto_now_add=False, null=True, blank=True, default='2021-12-12')
    isDelivered = models.BooleanField(default=False)
    shippingDate = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f" Order: {self.id} Shipped: {self.shippingDate}"


class OrderItem(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    make = models.CharField(max_length=30, null=True, blank=True)
    model = models.CharField(max_length=30, null=True, blank=True)
    VIN = models.CharField(max_length=30, null=True, blank=True)
    priceSold = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.VIN)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    dealername = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.address)
