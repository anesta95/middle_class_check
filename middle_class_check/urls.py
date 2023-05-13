from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("locales/", views.locales, name="locales"),
    path("results/", views.results, name="results")
]

