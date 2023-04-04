
from django.urls import path
from . import views

urlpatterns = [
    path('bar/', views.list_bar, name="list_bar"),
]
