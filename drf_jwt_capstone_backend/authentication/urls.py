from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UpdateUserProfile
from . import views
from vehicle.views import getUserProfile, getUserById, updateUser

urlpatterns = [

   

    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('get_users/', views.get_users, name='get_users'),
    path('profile/', getUserProfile, name="user-profiles"),
    path('profile/update/', views.UpdateUserProfile, name='users-profile-update'),

]