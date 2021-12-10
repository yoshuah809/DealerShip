from django.contrib.auth import get_user_model
from django.http.response import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer, RegistrationSerializer, UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
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
