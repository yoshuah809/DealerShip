from django.urls import path
from vehicle import views

urlpatterns = [

    #path('', views.getRoutes, name="routes"),
    path('vehicles/', views.getVehicles, name="vehicles"),
    path('users/profile/', views.getUserProfile, name="user-profiles"),
    path('users/', views.getUsers, name="users"),
    path('vehicles/<int:id>', views.getVehicle, name="vehicle"),
    path('orders/add', views.addOrderItems, name="add-orders"),
]
127
