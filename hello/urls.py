from django.urls import path
from . import views

# we give name to easily reference it from the other parts of the application
urlpatterns = [
    path("", views.index, name="index"),
    path("malay/", views.malay, name="malay"),
    path("<str:name>", views.greet, name="greet")
]