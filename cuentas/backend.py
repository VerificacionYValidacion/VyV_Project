from django.contrib.auth.backends import BaseBackend
from cuentas.models import Usuario


class UsuarioAutenticacionBackend(BaseBackend):
    def authenticate(self, username=None, contrasenia=None):
        try:
            usuario = Usuario.objects.get(correo_electronico=username)
            if usuario.check_password(contrasenia):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(correo_electronico=user_id)
        except:
            return None
