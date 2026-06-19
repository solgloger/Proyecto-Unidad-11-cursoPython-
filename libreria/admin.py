from django.contrib import admin
from .models import Autor, Categoria, Libro
# Register your models here.

@admin.register (Autor)
class AutorAdmin (admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")

@admin.register (Categoria)
class CategoriaAdmin (admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

@admin.register (Libro)
class LibroAdmin (admin.ModelAdmin):
    list_display = ("titulo", "autor__nombre", "categoria__nombre", "fecha_publicacion", "disponible")
    search_fields = ("titulo", "autor__nombre", "categoria__nombre")
    list_filter = ("disponible",)



