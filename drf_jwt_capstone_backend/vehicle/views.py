from django.db import models
from rest_framework import serializers, status
from rest_framework.fields import DateTimeField
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password

from .models import Vehicle, Order, OrderItem, ShippingAddress
from .serializers import UserSerializerWithToken, VehicleSerializer, UserSerializer, OrderSerializer
#from django.contrib.auth.models import User
from django.http import JsonResponse
from drf_jwt_capstone_backend import data
from django.contrib.auth import get_user_model
User = get_user_model()


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

        'api/users/profile/'
        'api/users/'
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializerWithToken(user, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):

    user = request.user
    data = request.data

    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:

        # (1) Create order

        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            dealerFees=data['dealerFees'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice'],



        )

        # (2) Create shipping address

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            state=data['shippingAddress']['state'],
            dealername=data['shippingAddress']['dealerName'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
        )

        # (3) Create order items adn set order to orderItem relationship
        for i in orderItems:
            vehicle = Vehicle.objects.get(id=i['vehicle'])

            item = OrderItem.objects.create(
                vehicle=vehicle,
                order=order,
                make=vehicle.make,
                model=vehicle.model,
                VIN=vehicle.VIN,
                priceSold=i['price'],

            )

            # (4) Update stock by Marking vehicle as sold

            #vehicle.isSold = True
            vehicle.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):

    user = request.user

    try:
        order = Order.objects.get(id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            Response({'detail': 'Not authorized to view this order'},
                     status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, pk):
    today = date.today()
    order = Order.objects.get(id=pk)

    order.isPaid = True
    order.paidAt = today
    order.save()

    return Response('Order was paid')


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('User was deleted')


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    vehicle.delete()
    return Response('Vehicle Deleted')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateVehicle(request, pk):
    data = request.data
    vehicle = Vehicle.objects.get(id=pk)

    vehicle.make = data['make']
    vehicle.model = data['model']
    vehicle.mfr = data['mfr']
    vehicle.VIN = data['VIN']
    vehicle.number_of_doors = data['number_of_doors']
    vehicle.millage = data['millage']
    vehicle.vehicle_type = data['vehicle_type']
    vehicle.main_image = data['main_image']
    vehicle.purchased_date = data['purchased_date']
    vehicle.date_sold = data['date_sold']
    vehicle.fuel_type = data['fuel_type']
    vehicle.features = data['features']
    vehicle.rowseat = data['rowseat']
    vehicle.transmission = data['transmission']
    vehicle.price = data['price']
    vehicle.isSold = data['isSold']

    vehicle.save()

    serializer = VehicleSerializer(vehicle, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createVehicle(request):
    user = request.user

    vehicle = Vehicle.objects.create(
        user=user,
        make='Sample vehicle',
        model='sample model',
        price=19500,
        VIN='12385',
        mfr=2014,
        fuel_type='Gas',
        transmission='Automatic',
        color='Blue',
        number_of_doors=4,
        purchased_date='2001-01-01'

    )

    serializer = VehicleSerializer(vehicle, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    vehicleid = data['vehicleid']
    vehicle = Vehicle.objects.get(id=vehicleid)

    vehicle.image = request.FILES.get('main_image')
    vehicle.save()

    return Response('Image was uploaded')


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
