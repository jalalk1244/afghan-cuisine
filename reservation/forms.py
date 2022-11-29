from django import forms
from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    '''Form for the reservation model '''
    class Meta:
        model = Reservation
        fields = ('title', 'num_of_guest', 'date_picked', 'time_picked')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True,}),
            'num_of_guest': forms.NumberInput(attrs={'class': 'form-control', 'minlength': 1, 'maxlength': 10, 'required': True, 'type': 'number',}),
            'date_picked': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'time_picked': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': True,}),
        }