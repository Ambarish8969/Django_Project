from django.urls import path
from . import views

urlpatterns = [
    path("", views.ambi, name="home")
]
