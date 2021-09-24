from enum import Enum
from django.db import models
from cuentas.models import Usuario


class Sector(Enum):
    SUR = "Sur"
    CENTRO = "Centro"
    NORTE = "Norte"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Categoria(Enum):
    DANOS_EN_LA_VIA_PUBLICA = "Daños en la vía pública"
    DANOS_EN_ESPACIOS_PUBLICOS = "Daños en espacios públicos"
    ANIMALES_ABANDONADOS_EN_LA_VIA_PUBLICA = "Animales abandonados"
    BASURA_EN_LUGARES_INCORRECTOS = "Basura en lugares incorrectos"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Estado(Enum):
    PENDIENTE = "Pendiente"
    EN_PROCESO = "En proceso"
    FINALIZADO = "Finalizado"

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
    usuario_reporte = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    estado_reporte = models.CharField(max_length=40, choices=Estado.choices())
    observacion = models.CharField(max_length=500, null=True)

    def notificar_reporte_enviado(self):
        mensaje = 'Reporte enviado'
        return mensaje

    def cambiar_estado_reporte(self, nuevo_estado_reporte):
        estados = set(item.value for item in Estado)
        if nuevo_estado_reporte in estados:
            self.estado_reporte = nuevo_estado_reporte
            return True
        else:
            return False

    def notificar_estado_modificado(self):
        mensaje = 'Estado modificado'
        return mensaje