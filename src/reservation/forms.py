from dataclasses import field
from django import forms
from .models import Reservation

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReserveTableForm(forms.ModelForm):
    

    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }





