from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("libros/", views.LibroListView.as_view(), name="libros"),
    path("libros/<int:pk>/", views.LibroDetailView.as_view(), name="libro_detail"),
    path("libros/crear/", views.LibroCreateView.as_view(), name="libro_create"),
    path("libros/<int:pk>/editar/", views.LibroUpdateView.as_view(), name="libro_update"),
    path("libros/<int:pk>/eliminar/", views.LibroDeleteView.as_view(), name="libro_delete"),
]