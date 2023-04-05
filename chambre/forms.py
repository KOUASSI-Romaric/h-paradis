from django.forms import ModelForm
from .models import Chambre


class ProduitForm(ModelForm):
    class Meta:
        model = Chambre
        fields = '__all__'
