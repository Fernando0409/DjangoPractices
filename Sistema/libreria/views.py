from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
from django.http import HttpResponse


# Create your views here.
def incio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def libros(request):
    libros = Libro.objects.all() # Select mejorado
    return render(request, 'libros/index.html', {'libros': libros})


def crearLibro(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})


def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})


def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
