
from django.urls import path
from . import views

urlpatterns = [
    path('client', views.list_client, name="client"),
]
