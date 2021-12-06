from django.db import models
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Vehicle
from .serializers import VehicleSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from drf_jwt_capstone_backend import data


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/vehicle/getVehicles',
        'api/vehicle/create/',
        'api/vehicle/upload',
        'api/vehicle/top/',
        'api/vehicle/<id>/',
        'api/vehicle/delete/'
        'api/vehicle/<update>/<id>/',
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([AllowAny])
def getVehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def getVehicle(request, id):
    vehicles = Vehicle.objects.get(id=id)
    serializer = VehicleSerializer(vehicles, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_vehicle(request):
    print('User', f"{request.user.username}")
    if request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
