from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Dorilar
from users.models import Bemorlar
def bemor_detail(request: HttpRequest, id: int) -> HttpResponse:

    dorilar = Dorilar.objects.filter(bemor_id=id)
    

    context = {
        "bemor": Bemorlar.objects.get(id=id),
        "dorilar": dorilar
    }
    return render(request=request, template_name="bemor_detail.html", context=context)
    
            
        
       



