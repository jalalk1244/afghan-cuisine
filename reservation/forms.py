from django import forms
from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    '''Form for the reservation model '''
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone_num',
                  'num_of_guest', 'date_picked', 'time_picked')

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'required': True}),
            'phone_num': forms.NumberInput(
                attrs={'class': 'form-control', 'type': 'tel'}),
            'num_of_guest': forms.Select(
                attrs={'class': 'form-control', 'required': True}),
            'date_picked': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date', 'required': True}),
            'time_picked': forms.TimeInput(
                attrs={'class': 'form-control',
                       'type': 'time', 'required': True}),
        }
