from django.shortcuts import render
from .models import Familiar
# Create your views here.
from django.http import HttpResponse
 
def saludo(request):
    return HttpResponse("HOLA, MUNDO!")

def saludo_con_template(request):
    return render(request, "mi_primer_app/saludo.html")

def crear_familiar(request, nombre):
    if nombre is not None:
        nuevo_familiar=Familiar(
            nombre=nombre,
            apellido="ejemplo apellido",
            edad=30,
            fecha_nacimiento="2003-12-09",
            parentesco="primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_primer_app/crear_familiar.html", {"nombre":nombre})
