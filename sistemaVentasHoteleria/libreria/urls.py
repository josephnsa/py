from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('nosotros', views.nosotros, name='nosotros'),
    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('habitaciones/crear', views.crear_habitacion, name='crear'),
    path('habitaciones/editar', views.editar_view, name='editar'),
    path('habitaciones/operation_room', views.operation_room, name='operation_room'),
    path('habitaciones/seleccionado/<int:numero>/', views.seleccionado_room, name='seleccionado_room'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('inspeccion/cuarto/<int:reserva_id>/', views.crear_inspeccion, name='crear_inspeccion'),
    path('habitaciones/<int:room_id>/reserva/', views.reserva_habitacion, name='reserva_habitacion'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
