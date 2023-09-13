from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='Porfolio/static/images')
    categorias = models.ManyToManyField(Categoria)
    fecha_creacion = models.DateField()
    url = models.URLField(blank=True) 

    def __str__(self):
        return self.titulo
