from django.urls import path
from vehicle import views

urlpatterns = [

    path('', views.getRoutes, name="routes"),
    path('vehicles/', views.getVehicles, name="vehicles/"),
    path('vehicles/<int:id>', views.getVehicle, name="product"),
]
