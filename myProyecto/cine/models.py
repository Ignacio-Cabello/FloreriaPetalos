from django.db import models

# Create your models here.

class Pelicula(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    valor=models.IntegerField()
    descripcion=models.TextField()  
    stock=models.IntegerField()
    estado=models.TextField()
    imagen=models.ImageField(upload_to='pelis',null=True)

    def __str__(self):
        return self.name

