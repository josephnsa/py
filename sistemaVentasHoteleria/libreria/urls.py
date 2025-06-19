from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('nosotros', views.nosotros, name='nosotros'),
    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('habitaciones/crear', views.crear_habitacion, name='crear'),
    path('habitaciones/editar', views.editar, name='editar'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

]
