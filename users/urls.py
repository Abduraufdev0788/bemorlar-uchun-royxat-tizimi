from django.urls import path , include
from .views import bemorlar_royxati, add_user
from dorilar.views import bemor_detail

urlpatterns = [
    path("table/", bemorlar_royxati, name="table_name"),
    path("table/<int:id>/", bemor_detail ),
    path("add/", add_user, name="add_user"),
    path("drugs/", include("dorilar.urls")),
]
