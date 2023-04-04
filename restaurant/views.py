from django.shortcuts import render, redirect


# Create your views here.
def affichage_restaurant(request):
    return render(request, "index.html")
