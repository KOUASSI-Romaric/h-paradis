
from django.urls import path
from . import views

urlpatterns = [
    path('chambre', views.list_chambre, name="chambre"),
]
