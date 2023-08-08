from django.urls import path
from .views import render_post,publicacion_detail

app_name= 'blog'

urlpatterns = [
    path('',render_post,name="publicaciones"),
    path('<int:publicaciones_id>',publicacion_detail,name="publicaciones_detail")
]

