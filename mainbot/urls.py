from django.urls import path
from mainbot import views

urlpatterns = [
    path("callback", views.callback, name="callback"),
]