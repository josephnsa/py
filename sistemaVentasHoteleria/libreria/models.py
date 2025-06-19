from django.db import models

class CategoriaCuarto(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre


class Cuarto(models.Model):
    numero = models.CharField(max_length=10, unique=True, verbose_name="Número del cuarto")
    piso = models.IntegerField(verbose_name="Piso")
    categoria = models.ForeignKey(CategoriaCuarto, on_delete=models.SET_NULL, null=True, verbose_name="Categoría")
    capacidad = models.PositiveIntegerField(default=1, verbose_name="Capacidad de personas")
    
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del cuarto")
    servicios = models.TextField(
        blank=True,
        null=True,
        verbose_name="Servicios incluidos (separados por comas)",
        help_text="Ej: WiFi, TV, Aire acondicionado"
    )

    imagen = models.ImageField(
        upload_to='imagenes_cuartos/',
        blank=True,
        null=True,
        verbose_name="Imagen del cuarto"
    )

    precio_por_noche = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio por noche"
    )
    
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Cuarto"
        verbose_name_plural = "Cuartos"
        ordering = ['piso', 'numero']

    def __str__(self):
        return f"Cuarto {self.numero} - Piso {self.piso} ({'Disponible' if self.disponible else 'Ocupado'})"


class ReservaCuarto(models.Model):
    cuarto = models.ForeignKey(Cuarto, on_delete=models.CASCADE, verbose_name="Cuarto reservado")
    
    # Datos del cliente
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    dni_cliente = models.CharField(max_length=20, verbose_name="DNI del cliente")
    correo_cliente = models.EmailField(verbose_name="Correo electrónico", blank=True, null=True)
    telefono_cliente = models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True)
    
    fecha_inicio = models.DateField(verbose_name="Fecha de ingreso")
    fecha_salida = models.DateField(verbose_name="Fecha de salida")
    fecha_reserva = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la reserva")

    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones del cliente")

    class Meta:
        verbose_name = "Reserva de Cuarto"
        verbose_name_plural = "Reservas de Cuartos"
        ordering = ['-fecha_reserva']

    def __str__(self):
        return f"Reserva de {self.cuarto} por {self.nombre_cliente}"

    def save(self, *args, **kwargs):
        # Marcar el cuarto como no disponible al hacer una reserva
        if self.cuarto.disponible:
            self.cuarto.disponible = False
            self.cuarto.save()
        super().save(*args, **kwargs)
