from enum import Enum

from django.db import models

# Create your models here.
class Sector(Enum):
    SUR = "SUR"
    CENTRO = "CENTRO"
    NORTE = "NORTE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Categoria(Enum):
    DANOS_EN_LA_VIA_PUBLICA = "DAÑOS EN LA VIA PUBLICA"
    DANOS_EN_ESPACIOS_PUBLICOS = "DAÑOS EN ESPACIOS PÚBLICOS"
    ANIMALES_ABANDONADOS_EN_LA_VIA_PUBLICA = "ANIMALES ABANDONADOS EN LA VÍA PÚBLICA"
    BASURA_EN_LUGARES_INCORRECTOS = "BASURA EN LUGARES INCORRECTOS"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Reporte(models.Model):
    sector_reporte = models.CharField(max_length=40, choices=Sector.choices())
    direccion_reporte = models.CharField(max_length=120)
    categoria_reporte = models.CharField(max_length=120, choices=Categoria.choices())
    evidencia_reporte = models.FileField(upload_to='uploads/%Y/%m/%d/')
    descripcion_reporte = models.CharField(max_length=240)

    def notificar_reporte_enviado(self):
        mensaje = 'Reporte enviado'
        return mensaje
