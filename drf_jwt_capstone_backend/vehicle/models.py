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
    VIN = models.CharField(max_length=50)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    mfr = models.IntegerField()
    color = models.CharField(max_length=20)
    vehicle_type = models.ForeignKey(
        Vehicle_Type, default=1, on_delete=models.PROTECT)
    main_image = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True)
    image3 = models.ImageField(upload_to='images', blank=True)
    purchased_date = DateField()
    date_sold = DateField(blank=True, null=True)
    fuel_type = models.ForeignKey(
        Fuel_Type, default=1, on_delete=models.PROTECT)
    features = models.CharField(max_length=100)
    number_of_doors_choices = (
        (2, 2),
        (4, 4),
        (6, 6),
    )
    number_of_doors = models.IntegerField(
        choices=number_of_doors_choices, default=4)

    rowseat_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
    )
    rowseat = models.IntegerField(choices=rowseat_choices, default=2)
    transmission_type_choices = (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    transmission = models.CharField(
        max_length=20, choices=transmission_type_choices, default='Automatic')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    isSold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.make} {self.model} {self.mfr}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=30, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    shippingDate = models.DateTimeField()
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
    image = models.CharField(max_length=200, null=True, blank=True)
    priceSold = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.VIN)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.address)
