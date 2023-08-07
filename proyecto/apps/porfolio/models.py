from django.db import models
from django.db.models.fields import CharField,URLField
from django.db.models.fields.files import ImageField

class Proyecto(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=500)
    img = ImageField(upload_to="porfolio/imgs/")
    url = URLField(blank = True)