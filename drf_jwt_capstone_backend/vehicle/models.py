from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, DateField


# Create your Models here.
class Vehicle_Type(models.Model):
    vehicle_type=models.CharField(max_length=15)

class Fuel_Type(models.Model):
    fuel_type=models.CharField(max_length=20)

number_of_doors_choices = (   
    (2,2),
    (4,4),  
    (6,6),
)
rowseat_choices = (   
    (1,1),
    (2,2),
    (3,3),
)

transmission_type_choices = (
    ('Automatic','Automatic'),
    ('Manual','Manual'),
)
class Vehicle(models.Model):
    User = get_user_model()
    VIN = models.CharField(max_length=50)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    mfr = models.IntegerField()
    color = models.CharField(max_length=20)
    type = models.ForeignKey(Vehicle_Type, default='Sedan', on_delete=models.PROTECT)
    purchased_date = DateField()
    date_sold = DateField(blank=True, null=True)
    fuel_type = models.ForeignKey(Fuel_Type, default='Gas', on_delete=models.PROTECT)
    features = models.CharField(max_length=100)
    number_of_doors = models.IntegerField(choices=number_of_doors_choices, default=4)
    rowseat = models.IntegerField(choices=rowseat_choices, default=2)
    transmission = models.CharField(max_length= 20, choices=transmission_type_choices, default='Automatic')

    def __str__(self):
       return f"{self.make} {self.model} {self.mfr}"