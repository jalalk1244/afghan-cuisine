from . import views
from django.urls import path

urlpatterns = [
    path('reservations', views.ReservationList.as_view(), name='reservations')
]