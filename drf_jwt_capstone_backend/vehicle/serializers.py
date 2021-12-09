from rest_framework import serializers
from .models import Vehicle
from django.contrib.auth import get_user_model


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


 