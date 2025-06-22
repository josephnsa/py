from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from libreria.models import RoomReservation
from django.db.models import Q
from django.db import models 
from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

def inicio(request):
    return render(request, 'paginas/Inicio.html')
    
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def habitaciones(request):
    return render(request, 'habitaciones/index.html')



def crear_habitacion(request):
    reservas = RoomReservation.objects.select_related('room', 'customer')

    codigo = request.GET.get('codigo')
    fecha_ingreso = request.GET.get('fechaIngreso')
    fecha_salida = request.GET.get('fechaSalida')
    tipo_habitacion = request.GET.get('tipoHabitacion')

    if codigo:
        reservas = reservas.filter(code__icontains=codigo)
    if fecha_ingreso:
        reservas = reservas.filter(check_in__gte=fecha_ingreso)
    if fecha_salida:
        reservas = reservas.filter(check_out__lte=fecha_salida)
    if tipo_habitacion:
        reservas = reservas.filter(room__tipo=tipo_habitacion)

    # Adaptar los campos al template
    reservas = reservas.values(
        codigo_reserva=models.F('code'),
        cuarto=models.F('room'),
        nombre_cliente=models.F('customer__full_name'),
        fecha_ingreso=models.F('check_in'),
        fecha_salida=models.F('check_out'),
        fecha_reserva=models.F('created_at')
    )

    context = {
        'reservas': reservas
    }
    return render(request, 'habitaciones/crear.html', context)


def editar(request):
    return render(request, 'habitaciones/editar.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('inicio')
#         else:
#             messages.error(request, 'Usuario o contraseña incorrectos.')

#     return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


