from django.db import models


class Client(models.Model):
    numero_cni = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.email
