from django.shortcuts import render
from Fambd.models import Fam

def addFamily(request):
    new_Fam= Fam.objects.create(name= "Pepito Gonzales", age= 49)
    context = {
        "new_Fam": new_Fam
    }
    return render(request, "add-family.html", context=context)

def Family(request):
    family= Fam.objects.all()
    context = {
        "family":family
    }
    return render(request, "family.html", context=context)
