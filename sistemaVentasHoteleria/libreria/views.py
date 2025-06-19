from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import CustomUserCreationForm

def inicio(request):
    return render(request, 'paginas/Inicio.html')
    
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def habitaciones(request):
    return render(request, 'habitaciones/index.html')

def crear_habitacion(request):
    return render(request, 'habitaciones/crear.html')

def editar(request):
    return render(request, 'habitaciones/editar.html')

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


