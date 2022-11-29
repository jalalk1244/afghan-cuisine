from django import forms
from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    '''Form for the reservation model '''
    class Meta:
        model = Reservation
        fields = ('title', 'num_of_guest', 'date_picked', 'time_picked')