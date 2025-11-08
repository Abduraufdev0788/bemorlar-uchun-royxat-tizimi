from django.urls import path , include
from .views import bemorlar_royxati, add_user
from dorilar.views import drug_view

urlpatterns = [
    path("table/", bemorlar_royxati, name="table_name"),
    path("table/<int:id>/", drug_view, name="drug_view"),
    path("add/", add_user, name="add_user"),
    path("", include("dorilar.urls")),
]
