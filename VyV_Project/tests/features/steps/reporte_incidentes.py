import random

from faker import Faker
from behave import *

from cuentas.models import Usuario
from reportes.models import Reporte, Sector, Categoria

use_step_matcher("re")


@step("que el señor Bryan tiene una sesión activa en la pantalla de Reportar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    usuario = Usuario.objects.get(correo_electronico='bryan.galindo@gmail.com')
    assert usuario.is_authenticated is True

@step('reporta un problema con: el "sector", "dirección","categoría","evidencia","descripción" del problema')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    faker = Faker(['en-US'])
    context.reporte = Reporte(Sector.SUR, faker.address(), Categoria.DANOS_EN_ESPACIOS_PUBLICOS, faker.file_name(category='image'), faker.text())
    assert isinstance(context.reporte, Reporte)


@step('el señor Bryan debe visualizar el mensaje "Reporte enviado" en color verde')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.mensaje = context.reporte.notificar_reporte_enviado()
    assert context.mensaje == "Reporte enviado"

