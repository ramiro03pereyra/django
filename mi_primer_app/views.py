from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def saludo(request):
    return HttpResponse("HOLA, MUNDO!")

def saludo_con_template(request):
    return render(request, "mi_primer_app/saludo.html")

