from django.db import models
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Vehicle
from .serializers import VehicleSerializer
from django.contrib.auth.models import User


class VehicleList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        vehicles=Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)