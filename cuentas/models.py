from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre_usuario = models.CharField(max_length=40)
    apellido_usuario = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=40, unique=True)

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_usuario', 'apellido_usuario', 'fecha_nacimiento', ]


class Sector(Enum):
    SUR = "SUR"
    CENTRO = "CENTRO"
    NORTE = "NORTE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Categoria(Enum):
    DANOS_EN_LA_VIA_PUBLICA = "DANOS_EN_LA_VIA_PUBLICA"
    DANOS_EN_ESPACIOS_PUBLICOS = "DANOS_EN_ESPACIOS_PUBLICOS"
    ANIMALES_ABANDONADOS_EN_LA_VIA_PUBLICA = "ANIMALES_ABANDONADOS_EN_LA_VIA_PUBLICA"
    BASURA_EN_LUGARES_INCORRECTOS = "BASURA_EN_LUGARES_INCORRECTOS"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

