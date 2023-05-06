from django import forms
from django.forms import ModelChoiceField, ModelMultipleChoiceField, DateInput
from .models import Client, Chambre, Reservation, Service
from django.contrib.auth.models import User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['client', 'room', 'check_in_date', 'check_out_date', 'services']
        widgets = {
            'check_in_date': DateInput(attrs={'type': 'date'}),
            'check_out_date': DateInput(attrs={'type': 'date'}),
        }

    client = ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    room = ModelChoiceField(queryset=Chambre.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    services = ModelMultipleChoiceField(queryset=Service.objects.all(), required=False, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
