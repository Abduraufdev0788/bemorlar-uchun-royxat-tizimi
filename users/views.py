from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Bemorlar


def add_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = request.POST
        new_bemor = Bemorlar(
            name=form.get("name"),
            age=form.get("age"),
            gender=form.get("gender"),
            diagnosis=form.get("diagnosis"),
            doctor_name=form.get("doctor_name"),
        )
        new_bemor.save()
        return redirect("table_name")
    return render(request=request, template_name="add_user.html")

def bemorlar_royxati(request: HttpRequest) -> HttpResponse:
    bemorlar = Bemorlar.objects.all()
    context = {
        "bemorlar": bemorlar
    }
    return render(request=request, template_name="user_table.html", context=context)

    
