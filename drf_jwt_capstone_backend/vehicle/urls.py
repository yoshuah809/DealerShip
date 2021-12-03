from django.urls import path
from vehicle import views

urlpatterns = [
    path('', views.VehicleList.as_view())
]