from django.shortcuts import render


# Create your views here.
def list_services(request):
    return render(request, 'services.html')
