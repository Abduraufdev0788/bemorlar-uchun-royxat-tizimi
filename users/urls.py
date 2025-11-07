from django.urls import path
from .views import bemorlar_royxati, add_user

urlpatterns = [
    path("", bemorlar_royxati, name="table_name"),
    path("add/", add_user, name="add_user"),
]
