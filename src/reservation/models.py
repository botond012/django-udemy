from os import name
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def only_int(value): 
        if value.isdigit()==False:
            raise ValidationError('ID contains characters')

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20,validators=[only_int])
    number_of_person = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

    