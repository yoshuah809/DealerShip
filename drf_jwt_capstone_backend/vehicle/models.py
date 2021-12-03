from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField, DateField


# Create your Models here.
type_choices = (

    ('Sedan', 'Sedan'),
    ('Coupe','Coupe'),
    ('Truck','Truck'),
    ('SUV', 'SUV'),
    ('Bus','Bus'),
    ('Collection', 'Collection'),
)
number_of_doors_choices = (   
    ('2', '2'),
    ('4','4'),  
    ('6','6'),
)
rowseat_choices = (   
    ('1','1'),
    ('2','2'),
    ('3','3'),
)
fueltype_choices =(
    ('Gas','Gas'),
    ('Diesel','Diesel'),
    ('Hybrid','Hybrid'),
    ('Electric','Electric'),
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
    type = models.CharField(max_length=15, choices=type_choices)
    purchased_date = DateField()
    date_sold = DateField()
    fuel_type = models.CharField(max_length=15, choices=fueltype_choices)
    features = models.CharField(max_length=100)
    number_of_doors = models.CharField(max_length=15, choices=number_of_doors_choices)
    rowseat = models.IntegerField(choices=rowseat_choices)
    transmission = models.CharField(max_length= 20, choices=transmission_type_choices)