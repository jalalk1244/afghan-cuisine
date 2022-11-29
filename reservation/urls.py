from . import views
from django.urls import path

urlpatterns = [
    path('reservations', views.ReservationList.as_view(), name='reservations'),
    path('create_reservation', views.create_reservation, name='create_reservation'),
]