from behave import *

from cuentas.models import Usuario
from reportes.models import Reporte

use_step_matcher("re")


@step("que Isac tiene una cuenta de administrador")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    usuario = Usuario.objects.get(correo_electronico='isac.rivas@gmail.com')
    assert usuario.is_superuser is True


@step('existen reportes con estado "Pendiente"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reportes_pendientes = Reporte.objects.filter(estado_reporte="Pendiente")
    assert context.reportes_pendientes.count() > 0


@step('cambia el estado de un reporte "Pendiente" a "En proceso"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reporte = context.reportes_pendientes[0]
    assert context.reporte.cambiar_estado_reporte('En proceso')


@step('Isac debe visualizar el mensaje "Estado modificado" en color verde')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.mensaje = context.reporte.notificar_estado_modificado()
    assert context.mensaje == "Estado modificado"


@step('existen reportes con estado "En proceso"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reportes_en_proceso = Reporte.objects.filter(estado_reporte="En proceso")
    assert context.reportes_en_proceso.count() > 0


@step('cambia el estado de un reporte "En Proceso" a "Finalizado"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reporte = context.reportes_en_proceso[0]
    assert context.reporte.cambiar_estado_reporte('Finalizado')

