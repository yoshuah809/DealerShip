from django.urls import path
from vehicle import views

urlpatterns = [

    #path('', views.getRoutes, name="routes"),
    path('vehicles/', views.getVehicles, name="vehicles"),
    path('users/profile/', views.getUserProfile, name="user-profiles"),
    path('users/delete/<str:pk>/', views.deleteUser, name="user-delete"),
    path('users/', views.getUsers, name="users"),

    path('users/<str:pk>/', views.getUserById, name="user"),
    path('users/update/<str:pk>/', views.updateUser, name="user-update"),

    path('vehicles/create/', views.createVehicle, name="vehicle-create"),
    path('vehicles/<int:id>', views.getVehicle, name="vehicle"),
    path('orders/add/', views.addOrderItems, name="get-order"),
    path('orders/myorders/', views.getMyOrders, name="my-orders"),

    path('orders/<str:pk>/', views.getOrderById, name="user-order"),
    path('orders/<str:pk>/pay/', views.updateOrderToPaid, name="pay-order"),

    path('vehicles/update/<str:pk>/', views.updateVehicle, name="vehicle-update"),
    path('vehicles/delete/<str:pk>/', views.deleteVehicle, name="vehicle-delete"),
]
