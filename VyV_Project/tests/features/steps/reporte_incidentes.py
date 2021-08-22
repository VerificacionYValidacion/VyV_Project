import random

from behave import *

use_step_matcher("re")


@step("que el señor Bryan tiene una sesión activa en la pantalla de Reportar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    usuario = Usuario.object.get(username="Bryan")
    assert usuario.is_authenticated


@step('reporta un problema con: el "sector", "dirección","categoría","evidencia","descripción" del problema')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reporte = Reporte(Sector.SUR, faker.address, Categoria.DANOS_EN_ESPACIOS_PUBLICOS, faker.file, faker.lorem)
    assert isinstance(reporte, Reporte)


@step('el señor Bryan debe visualizar el mensaje "Reporte enviado" en color verde')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.reporte.es_completado():
        context.mensaje = context.reporte.notificar()
        assert context.mensaje == "Reporte enviado"
    else:
        assert True


@step(
    'si el formulario está incompleto, el señor Bryan debe visualizar el mensaje "Debe llenar los campos correctamente" en color rojo')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    if context.reporte.es_completado():
        assert True
    else:
        mensaje = context.reporte.notificar_campos_incorrectos()
        assert mensaje == "Debe llenar los campos correctamente"
