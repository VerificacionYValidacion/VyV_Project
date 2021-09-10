from behave import *

from cuentas.models import Usuario
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from reportes.models import Reporte

use_step_matcher("re")


@step("que Isac tiene una cuenta de administrador")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    usuario = Usuario.objects.get(correo_electronico='isac.rivas@gmail.com')
    assert usuario.is_superuser is True


@step('ingresa en la sección de "Reportes"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    validate = URLValidator()
    try:
        validate('http://127.0.0.1:8000/lista_reportes')
        is_valid = True
    except ValidationError:
        is_valid = False

    assert is_valid is True


@step("puede cambiar el estado de un reporte de la lista para darle seguimiento")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    reporte = Reporte.objects.get(pk=8)
    reporte.cambiar_estado(nuevo_estado)
