from django.shortcuts import render


# Create your views here.

def list_chambre(request):

    return render(request, 'hotel.html')
