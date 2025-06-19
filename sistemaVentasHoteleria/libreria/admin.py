from django.contrib import admin
from .models import CategoriaCuarto, Cuarto, ReservaCuarto

@admin.register(CategoriaCuarto)
class CategoriaCuartoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(Cuarto)
class CuartoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'piso', 'categoria', 'capacidad', 'precio_por_noche', 'disponible']
    list_filter = ['disponible', 'categoria']
    search_fields = ['numero', 'categoria__nombre']
    list_editable = ['disponible']


@admin.register(ReservaCuarto)
class ReservaCuartoAdmin(admin.ModelAdmin):
    list_display = ['cuarto', 'nombre_cliente', 'fecha_inicio', 'fecha_salida', 'fecha_reserva']
    search_fields = ['nombre_cliente', 'dni_cliente', 'cuarto__numero']
    list_filter = ['fecha_inicio', 'fecha_salida']
