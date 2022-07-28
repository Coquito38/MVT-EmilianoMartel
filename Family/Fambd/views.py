from django.shortcuts import render
from Fambd.models import Fam

def addFamily(request):
    new_Fam= Fam.objects.create(name= "Carlos Martel", age= 57)
    context = {
        "new_Fam": new_Fam
    }
    return render(request, "add-family.html", context=context)

def Family(request):
    Family1= Fam.objects.all()
    context = {
        "Family":Family1
    }
    return render(request, "family.html", context=context)
