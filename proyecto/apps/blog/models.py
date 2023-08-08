from django.db import models
import datetime 
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='blog/imgs')
    año = models.DateField(datetime.date.today)
