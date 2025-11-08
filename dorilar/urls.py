from django.urls import path
from .views import add_drug, drug_view

urlpatterns = [
    path("drug_view", drug_view, name="drug_view"),
    path("drug_view/<int:bemor_id>/", add_drug, name="add_drug"),                
]
