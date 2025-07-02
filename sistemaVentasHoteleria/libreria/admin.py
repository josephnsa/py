from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Room,
    RoomCategory,
    RoomType,
    RoomStatus,
    BedType,
    Amenity,
    RoomAmenity,
    Customer,
    RoomReservation,
    ReservationSource,
    Service,
    RoomService,
    Payment,
    Staff,
    DocumentType,
    RoomMaintenance,
    RoomChangeLog,
    ReservationHistory,
    CustomUser,
    Region,
    Province,
    District,
    RoomInspectionReport
)
from libreria.models import Cuarto, ReservaCuarto, CategoriaCuarto

# ------------------------------
# Sección: Habitaciones
# ------------------------------
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'type', 'status', 'available')
    list_filter = ('type', 'status', 'floor')
    search_fields = ('number',)

admin.site.register(RoomCategory)
admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(BedType)
admin.site.register(Amenity)
admin.site.register(RoomAmenity)

# ------------------------------
# Sección: Reservas
# ------------------------------
@admin.register(RoomReservation)
class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ('code', 'customer_name', 'room', 'status', 'check_in', 'check_out')
    search_fields = ('code', 'customer_name', 'customer_document', 'room__number')
    list_filter = ('status', 'room')

admin.site.register(ReservationSource)

# ------------------------------
# Sección: Clientes y Staff
# ------------------------------
admin.site.register(Customer)
admin.site.register(Staff)

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'name')
    search_fields = ('name', 'abbreviation')

# ------------------------------
# Sección: Servicios y Pagos
# ------------------------------
admin.site.register(Service)
admin.site.register(RoomService)
admin.site.register(Payment)

# ------------------------------
# Mantenimiento y Historial
# ------------------------------
admin.site.register(RoomMaintenance)
admin.site.register(RoomChangeLog)
admin.site.register(ReservationHistory)

# ------------------------------
# Usuario personalizado
# ------------------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'dni', 'is_staff', 'region', 'district')
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('dni', 'phone', 'address', 'region', 'district', 'email_confirmed', 'accepted_terms')
        }),
    )



@admin.register(RoomInspectionReport)
class RoomInspectionReportAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'room', 'estado_general', 'creado_en')
    search_fields = ('reservation__code', 'room__number')
    list_filter = ('estado_general',)
# ------------------------------
# Ubicación geográfica
# ------------------------------
admin.site.register(Region)
admin.site.register(Province)
admin.site.register(District)

# ------------------------------
# Modelos adicionales
# ------------------------------
admin.site.register(Cuarto)
admin.site.register(ReservaCuarto)
admin.site.register(CategoriaCuarto)
