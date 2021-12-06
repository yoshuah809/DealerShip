from django.urls import path
from vehicle import views

urlpatterns = [

    path('', views.getRoutes, name="routes"),
    path('vehicles/', views.getVehicles, name="products"),
    path('vehicles/<int:id>', views.getVehicle, name="product"),
]
