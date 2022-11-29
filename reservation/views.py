from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm


class ReservationList(View):

    def get(self, request, *args, **kwargs):
        reservations_list = Reservation.objects.filter(client=request.user).order_by('-date_picked')

        return render(
            request, 
            'view_reservations.html',
            {
                'reservations_list': reservations_list
            },
            )


def create_reservation(request):
    submitted = False
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.instance.client = request.user
            reservation_form.instance.approved = False
            reservation_form.save()
            return HttpResponseRedirect('/create_reservation?submitted=True')
    else:
        reservation_form = ReservationForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'create_reservation.html', {'form': reservation_form, 'submitted':submitted})