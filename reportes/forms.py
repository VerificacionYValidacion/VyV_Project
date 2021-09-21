from django import forms

from cuentas.models import Usuario
from reportes.models import Reporte


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ('sector_reporte', 'direccion_reporte', 'categoria_reporte', 'evidencia_reporte', 'descripcion_reporte')
        widgets = {
            'sector_reporte': forms.Select(attrs={'class': 'form-select form-control'}),
            'direccion_reporte': forms.TextInput(attrs={'class': 'form-control', 'empty_label': 'Select One', 'placeholder': 'Ejm. La Floresta'}),
            'categoria_reporte': forms.Select(attrs={'class': 'form-select form-control'}),
            'evidencia_reporte': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion_reporte': forms.Textarea(attrs={'placeholder': ' Descripción del problema'}),
        }
        labels = {
            'sector_reporte': 'Selecciona el sector del problema',
            'direccion_reporte': 'Ingresa la dirección del problema',
            'categoria_reporte': 'Selecciona la categoría del problema',
            'evidencia_reporte': 'Adjunta evidencia del problema',
            'descripcion_reporte': 'Describe el problema'
        }

