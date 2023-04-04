from django.urls import path
from . import views

urlpatterns = [
    path('service', views.list_services, name="list_services"),
]
