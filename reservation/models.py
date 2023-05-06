from django.db import models
from chambre.models import Chambre
from client.models import Client
from service.models import Service


# Create your models here.
class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    services = models.ManyToManyField(Service, blank=True)


    def __str__(self):
        return f"{self.client.name} - {self.room.name}"
