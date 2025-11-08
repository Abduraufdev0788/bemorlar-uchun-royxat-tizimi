from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Dorilar
from users.models import Bemorlar
def drug_view(request: HttpRequest, id: int) -> HttpResponse:

    dorilar = Dorilar.objects.filter(bemor_id=id)
    

    context = {
        "bemor": Bemorlar.objects.get(id=id),
        "dorilar": dorilar
    }
    return render(request=request, template_name="bemor_detail.html", context=context)

def add_drug(request: HttpRequest, bemor_id: int) -> HttpResponse:
    bemor = get_object_or_404(Bemorlar, id=bemor_id)

    if request.method == "POST":
        new_dori = Dorilar(
            bemor = bemor,
            dori_name = request.POST.get("dori_name"),
            description = request.POST.get("description"),
            once_in_day = request.POST.get("once_in_day"),
            dosage = request.POST.get("dosage"),
            usage_time = request.POST.get("usage_time"),
            doctor_name = request.POST.get("doctor_name"),
            created_at = request.POST.get("created_at"),
            finish_at = request.POST.get("finish_at"),
            is_active = request.POST.get("is_active") == "on",
                )

        new_dori.save()

        return redirect("bemor_detail", id=bemor_id)
    
    return render(request, "add_drug.html", {"bemor": bemor})

        
        
    
            
        
       



