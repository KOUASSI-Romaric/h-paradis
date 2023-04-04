from django.shortcuts import render, redirect
from .models import Client, Chambre, Reservation, Service
from .forms import ReservationForm


def home(request):

    return render(request, 'index.html')


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            room_id = request.POST.get('room')
            room = Chambre.objects.get(id=room_id)
            reservation.room = room
            client_id = request.POST.get('client')
            client = Client.objects.get(id=client_id)
            reservation.client = client
            reservation.save()
            form.save_m2m()
            return redirect('/')
    else:
        '''room_id ='' # request.GET.get('room')
        room = "" #Chambre.objects.get(id=room_id)
        client_id = request.GET.get('client')
        client = Client.objects.get(id=client_id)'''
        form = ReservationForm()#initial={'room': room, 'client': client}
    context = {'form': form}
    return render(request, 'reservationform.html', context)
