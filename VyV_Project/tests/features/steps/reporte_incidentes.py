from behave import *

use_step_matcher("re")


@step("que el señor Bryan tiene una sesión activa")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que el señor Bryan tiene una sesión activa')


@step("en la pantalla Inicio selecciona la opción de Reportar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando en la pantalla Inicio selecciona la opción de Reportar')


@step('especifica lo siguiente: el "sector", "dirección","tipo","evidencia","descripción" del problema o incidente')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Y especifica lo siguiente: el "sector", "dirección","tipo","evidencia","descripción" del problema o incidente')


@step('selecciona el botón "Enviar"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y selecciona el botón "Enviar"')


@step("estos datos deben ser guardados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Entonces estos datos deben ser guardados')


@step('el señor Bryan debe visualizar el mensaje "Reporte enviado" en color verde')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y el señor Bryan debe visualizar el mensaje "Reporte enviado" en color verde')


@step(
    'si el formulario está incompleto, el señor Bryan debe visualizar el mensaje "Debe llenar todos los campos" en color rojo')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Pero si el formulario está incompleto, el señor Bryan debe visualizar el mensaje "Debe llenar todos los campos" en color rojo')