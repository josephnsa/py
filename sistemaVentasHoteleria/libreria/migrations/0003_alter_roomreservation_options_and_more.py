# Generated by Django 5.2.3 on 2025-07-02 06:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_categoriacuarto_cuarto_reservacuarto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomreservation',
            options={'ordering': ['-created_at'], 'verbose_name': 'Reserva de Cuarto', 'verbose_name_plural': 'Reservas de Cuartos'},
        ),
        migrations.RemoveField(
            model_name='roomreservation',
            name='customer',
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='customer_document',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='customer_name',
            field=models.CharField(default='Desconocido', max_length=100, verbose_name='Nombre del cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='check_in',
            field=models.DateField(verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='check_out',
            field=models.DateField(verbose_name='Fecha de salida'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='code',
            field=models.CharField(editable=False, max_length=12, unique=True, verbose_name='Código de Reserva'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de reserva'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libreria.room', verbose_name='Cuarto reservado'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='status',
            field=models.CharField(choices=[('reservado', 'Reservado'), ('ocupado', 'Ocupado'), ('cancelado', 'Cancelado'), ('finalizado', 'Finalizado')], default='reservado', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Registrado por'),
        ),
    ]
