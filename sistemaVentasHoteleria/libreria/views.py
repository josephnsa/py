from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'paginas/Inicio.html')

def nosotros(request):
    return  render (request, 'paginas/nosotros.html')
def habitaciones(request):
    return  render (request, 'habitaciones/index.html')
def crear_habitacion(request):
    return render ( request, 'habitaciones/crear.html')
def editar(request):
    return render ( request, 'habitaciones/editar.html')