from django.shortcuts import render
from .models import Proyecto
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request,"profolio/home.html",{"proyectos": proyectos})
