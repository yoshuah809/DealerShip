from django.contrib.auth.hashers import make_password
from django.http.response import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer, RegistrationSerializer, UserSerializer, UserSerializerWithToken
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(User, many=True)
        return Response(serializer.data)
    except:
        User.DoesNotExist
        raise Http404


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.middle_name = data['middle_name']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(User, many=False)
    return Response(serializer.data)
