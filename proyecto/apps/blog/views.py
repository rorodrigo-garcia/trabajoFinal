from django.shortcuts import render , get_list_or_404
from .models import Publicaciones

def render_post(request):
    publicaciones = Publicaciones.objects.all()
    return render(request,"publicaciones.html", {"publicaciones" : publicaciones})

def publicacion_detail(request,publicaciones_id):
    publicacion = get_list_or_404(Publicaciones , pk=publicaciones_id)
    return render(request,"publicaciones_detail.html",{"publicaciones":publicacion})
