# forms.py

from django import forms
from .models import RoomReservation

class RoomReservationForm(forms.ModelForm):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = RoomReservation
        fields = [
            'customer_name', 'customer_document', 'customer_email', 'customer_phone',
            'check_in', 'check_out', 
        ]
