from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Libro
from .forms import LibroForm
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
# Create your views here.

def inicio(request):
    return render(request, "libreria/inicio.html")

class LibroListView (ListView):
    model = Libro 
    template_name = "libreria/libros_list.html"
    context_object_name = "libros"

    def get_queryset(self):
        query = self.request.GET.get("q")
        libros = Libro.objects.all()
        if query:
            libros = libros.filter(
                Q(titulo__icontains=query) |
                Q(autor__nombre__icontains=query) |
                Q(categoria__nombre__icontains=query)
            )
        return libros.order_by("titulo")

class LibroDetailView (DetailView):
    model = Libro 
    template_name = "libreria/libro_detail.html"
    context_object_name = "libro"

class LibroCreateView(PermissionRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libreria/libro_forms.html"
    permission_required = "libreria.add_libro"

    def get_success_url(self):
        return reverse_lazy("libros")

    
class LibroUpdateView (PermissionRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libreria/libro_forms.html"
    permission_required = "libreria.change_libro"
    success_url = reverse_lazy("libros")

class LibroDeleteView(PermissionRequiredMixin, DeleteView):
    model = Libro
    template_name = "libreria/libro_confirm_delete.html"
    permission_required = "libreria.delete_libro"
    success_url = reverse_lazy("libros")

