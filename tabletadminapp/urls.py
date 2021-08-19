from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("hozzadas/<int:napszam>", views.hozzadas,name="hozzadas"),
    path("bejelentkezes",views.bejelentkezes,name="bejelentkezes")
]
