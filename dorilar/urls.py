from django.urls import path
from .views import bemor_detail

urlpatterns = [
    path("", bemor_detail, name="bemor_detail"),
    
]