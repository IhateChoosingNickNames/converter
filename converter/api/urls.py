from django.urls import path

from . import views

APP_NAME = "api"

urlpatterns = [
    path("rates/", views.get_value),
]
