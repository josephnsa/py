# reservas/form1.py
from django import forms
from .models.reclamo import RoomInspectionReport  # o .models si no está dividido

class RoomInspectionReportForm(forms.ModelForm):
    class Meta:
        model = RoomInspectionReport
        exclude = ['reservation', 'room', 'category', 'creado_en']
        widgets = {
            'estado_general': forms.Select(attrs={'class': 'form-control'}),
            'observaciones_piso': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'observaciones_paredes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'observaciones_muebles': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'observaciones_servicios': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'limpieza_general': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'otros_detalles': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'evidencia_1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'evidencia_2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'evidencia_3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
