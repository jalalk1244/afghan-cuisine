from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm


class ReservationList(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            reservations_list = Reservation.objects.filter(client=request.user).order_by('-date_picked')
        else:
            reservations_list = []
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


def edit_reservation(request, reservation_id):
    query_set = Reservation.objects.filter(id=reservation_id)
    reservation = get_object_or_404(query_set, id=reservation_id)

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation.title = request.POST['title']
            reservation.num_of_guest = request.POST['num_of_guest']
            reservation.date_picked = request.POST['date_picked']
            reservation.time_picked = request.POST['time_picked']
            reservation.save()
            return HttpResponseRedirect('/reservations')
    else:
        reservation_data = {
        'title': reservation.title,
        'client': reservation.client,
        'num_of_guest': reservation.num_of_guest,
        'date_picked': reservation.date_picked,
        'time_picked': reservation.time_picked,
        'approved': reservation.approved,
        }
        reservation_form = ReservationForm(initial=reservation_data)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'edit_reservation.html', {'form': reservation_form})
