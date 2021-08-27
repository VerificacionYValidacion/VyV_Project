from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre_usuario = models.CharField(max_length=40)
    apellido_usuario = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(max_length=40, unique=True)

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre_usuario', 'apellido_usuario', 'fecha_nacimiento', ]
