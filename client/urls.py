
from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.contact, name="contact_us"),
]
