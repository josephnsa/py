from django.contrib import admin
from .models import CategoriaCuarto, Cuarto, ReservaCuarto


@admin.register(CategoriaCuarto)
class CategoriaCuartoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Cuarto)
class CuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'piso', 'categoria', 'capacidad', 'precio_por_noche', 'disponible')
    list_filter = ('piso', 'categoria', 'disponible')
    search_fields = ('numero',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    fieldsets = (
        ('Información General', {
            'fields': ('numero', 'piso', 'categoria', 'capacidad', 'descripcion', 'servicios')
        }),
        ('Multimedia y Estado', {
            'fields': ('imagen', 'precio_por_noche', 'disponible')
        }),
        ('Tiempos del Registro', {
            'fields': ('fecha_creacion', 'fecha_actualizacion')
        }),
    )


@admin.register(ReservaCuarto)
class ReservaCuartoAdmin(admin.ModelAdmin):
    list_display = ('codigo_reserva', 'nombre_cliente', 'cuarto', 'fecha_ingreso', 'fecha_salida', 'estado')
    list_filter = ('estado', 'fecha_ingreso', 'fecha_salida')
    search_fields = ('codigo_reserva', 'nombre_cliente', 'documento_cliente')
    readonly_fields = ('codigo_reserva', 'fecha_reserva')
    fieldsets = (
        ('Datos del Cliente', {
            'fields': ('nombre_cliente', 'documento_cliente', 'correo_cliente', 'telefono_cliente')
        }),
        ('Reserva', {
            'fields': ('cuarto', 'fecha_ingreso', 'fecha_salida', 'estado')
        }),
        ('Información del Sistema', {
            'fields': ('codigo_reserva', 'fecha_reserva')
        }),
    )
