from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from .models import Reservation



# def get_reservations(request, User):

#     current_client = request.user
#     reservations = Reservation.objects.filter(client=current_client).order_by('-date_picked')

#     return reservations

# class ReservationList(generic.ListView):
#     model = Reservation
#     queryset = Reservation.objects.filter(client=request.user).order_by('-date_picked')
#     template_name = 'reservations.html'


class ReservationList(View):

    def get(self, request, *args, **kwargs):
        reservations_list = Reservation.objects.filter(client=request.user).order_by('-date_picked')

        return render(
            request, 
            'reservations.html',
            {
                'reservations_list': reservations_list
            },
            )