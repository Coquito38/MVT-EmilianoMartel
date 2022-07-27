from django.shortcuts import render
from Fambd.models import Family

def addFamily(request):
    new_Fam= Family.objet.create(name= "Carlos Martel", age= 57)
    context = {
        "new_Fam": new_Fam
    }
    return render(request, "add-family.htm", context=context)

def Family(request):
    Family= Family.objet.all()
    context = {
        "Family":Family
    }
    return render(request, "family.html", context=context)
