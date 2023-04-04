from django.db import models


class ChambreCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Chambre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.IntegerField(null=True)
    category = models.ForeignKey(ChambreCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):

        return "{}".format(self.category)
