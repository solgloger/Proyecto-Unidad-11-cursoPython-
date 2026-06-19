from django.db import models

# Create your models here.
class Autor (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__ (self):
        return self.nombre
    
class Categoria (models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Libro (models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        Autor,
        on_delete= models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete= models.CASCADE
    )

    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
