from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from libreria.models import RoomReservation
from django.db.models import Q
from django.db import models 
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.utils import timezone
from libreria.models import Room, RoomReservation
# from .forms import CustomUserCreationForm
# from .forms import CustomUserCreationForm

def inicio(request):
    return render(request, 'paginas/Inicio.html')
    
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def habitaciones(request):
    return render(request, 'habitaciones/index.html')

def crear_habitacion(request):
    reservas = RoomReservation.objects.select_related('room')

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
        reservas = reservas.filter(room__type__name__icontains=tipo_habitacion)  # Ajusta según modelo RoomType

    context = {
        'reservas': reservas
    }
    return render(request, 'habitaciones/crear.html', context)


def editar(request):
    return render(request, 'habitaciones/editar.html')


def operation_room(request):
    hoy = timezone.now().date()
    rooms = []

    for room in Room.objects.all():
        # Verifica si tiene reserva activa hoy
        reserva = RoomReservation.objects.filter(
            room=room,
            status__in=['reservado', 'ocupado'],
            check_in__lte=hoy,
            check_out__gte=hoy
        ).first()

        # Estado según reserva o disponibilidad
        if reserva:
            estado = reserva.status.upper()  # RESERVADO / OCUPADO
        elif room.available:
            estado = 'DISPONIBLE'
        else:
            estado = 'NO DISPONIBLE'

        rooms.append({
            'numero': room.number,
            'estado': estado,
            'piso': room.floor,
            'categoria': room.category.name if room.category else 'N/A',
            'tipo_cama': room.bed_type.name if room.bed_type else 'N/A'
        })

    return render(request, 'habitaciones/operation-room.html', {'rooms': rooms})
def seleccionado_room(request, numero):
    room = get_object_or_404(Room, number=numero)

    reserva = RoomReservation.objects.filter(
        room=room,
        status__in=['reservado', 'ocupado']
    ).order_by('-created_at').first()  # trae la última reserva activa si existe

    return render(request, 'habitaciones/operation-creation.html', {
        'room': room,
        'reserva': reserva  # envía la reserva al template
    })

def login_view(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('inicio')
         else:
             messages.error(request, 'Usuario o contraseña incorrectos.')

     return render(request, 'usuarios/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')

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
