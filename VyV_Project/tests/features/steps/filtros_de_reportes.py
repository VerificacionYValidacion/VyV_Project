from behave import *

from reportes.models import Reporte, Categoria, Estado, Sector

use_step_matcher("re")


@step("existen reportes listados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.reportes = Reporte.objects.all()
    assert context.reportes.count() > 0


@step("selecciona una categoría para filtrar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    filtro_categoria = Categoria.BASURA_EN_LUGARES_INCORRECTOS
    reportes_filtrados = Reporte.filtro(filtro_categoria)
    categoria_verificada = Reporte.verificar_categoria(reportes_filtrados, filtro_categoria)
    assert categoria_verificada


@step("la tabla solo debe mostrar reportes de esa categoría para priorizarlos acorde a sus preferencias")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@step("selecciona un estado para filtrar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    filtro_estado = Estado.PENDIENTE
    reportes_filtrados = Reporte.filtro(filtro_estado)
    estado_verificada = Reporte.verificar_estado(reportes_filtrados, filtro_estado)
    assert estado_verificada


@step("la tabla solo debe mostrar reportes con ese estado para priorizarlos acorde a sus preferencias")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces la tabla solo debe mostrar reportes con ese estado para priorizarlos acorde a sus preferencias')


@step("selecciona un sector para filtrar")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    filtro_sector = Sector.NORTE
    reportes_filtrados = Reporte.filtro(filtro_sector)
    sector_verificado = Reporte.verificar_sector(reportes_filtrados, filtro_sector)
    assert sector_verificado


@step("la tabla solo debe mostrar reportes con de ese sector para priorizarlos acorde a sus preferencias")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Entonces la tabla solo debe mostrar reportes con de ese sector para priorizarlos acorde a sus preferencias')