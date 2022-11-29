from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .models import Reservation



def get_reservations(self, request, User):

    current_client = request.user
    reservations = Reservation.objects.filter(client=current_client).order_by('-date_picked')

    return reservations

class ReservationList(generic.ListView):
    model = Reservation
    queryset = get_reservations(self, request, User)
    template_name = 'reservations.html'
