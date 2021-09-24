from django.shortcuts import render, redirect

from cuentas.models import Usuario
from .forms import ReporteForm
from .models import Reporte
from .models import Estado
from django.contrib import messages


def index(request):
    form_class = ReporteForm()
    reporte = Reporte()
    if request.method == 'POST':
        form_class = ReporteForm(request.POST, request.FILES)
        usuario = Usuario.objects.get(correo_electronico='bryan.galindo@gmail.com')
        if form_class.is_valid() & usuario.is_authenticated:
            form_reporte = form_class.save(commit=False)
            form_reporte.usuario_reporte = usuario
            form_reporte.estado_reporte = Estado.PENDIENTE.value
            form_class.save()
            messages.success(request, reporte.notificar_reporte_enviado())
            form_class = ReporteForm()
        else:
            print("Form no valido")

    context = {'form': form_class}
    return render(request, 'reporte_modelform.html', context)


def lista_reportes(request):
    if 'filtro' in request.POST:
        reportes_pendientes = []
        reportes_en_proceso = []
        reportes_finalizados = []
        print(request.POST['select_estado'])
        print(request.POST['select_sector'])
        print(request.POST['select_categoria'])

        if request.POST['select_estado'] != "null" and request.POST['select_sector'] != "null" and request.POST['select_categoria'] != "null":
            reportes_filtrados = Reporte.objects.filter(estado_reporte=request.POST['select_estado'],
                                                        sector_reporte=request.POST['select_sector'],
                                                        categoria_reporte=request.POST['select_categoria'])

        elif request.POST['select_estado'] != "null" and request.POST['select_sector'] != "null":
            reportes_filtrados = Reporte.objects.filter(estado_reporte=request.POST['select_estado'],
                                                        sector_reporte=request.POST['select_sector'])
        elif request.POST['select_estado'] != "null" and request.POST['select_categoria'] != "null":
            reportes_filtrados = Reporte.objects.filter(estado_reporte=request.POST['select_estado'],
                                                        categoria_reporte=request.POST['select_categoria'])

        elif request.POST['select_sector'] != "null" and request.POST['select_categoria'] != "null":
            reportes_filtrados = Reporte.objects.filter(sector_reporte=request.POST['select_sector'],
                                                        categoria_reporte=request.POST['select_categoria'])
        elif request.POST['select_estado'] != "null":
            reportes_filtrados = Reporte.objects.filter(estado_reporte=request.POST['select_estado'])

        elif request.POST['select_sector'] != "null":
            reportes_filtrados = Reporte.objects.filter(sector_reporte=request.POST['select_sector'])
            reportes_pendientes = reportes_filtrados

        elif request.POST['select_categoria'] != "null":
            reportes_filtrados = Reporte.objects.filter(categoria_reporte=request.POST['select_categoria'])
            reportes_pendientes = reportes_filtrados

        else:
            reportes_pendientes = Reporte.objects.filter(estado_reporte='Pendiente').order_by('-id')
            reportes_en_proceso = Reporte.objects.filter(estado_reporte='En proceso')
            reportes_finalizados = Reporte.objects.filter(estado_reporte='Finalizado')

        if request.POST['select_estado'] == 'Pendiente':
            reportes_pendientes = reportes_filtrados
        elif request.POST['select_estado'] == 'En proceso':
            reportes_en_proceso = reportes_filtrados
        elif request.POST['select_estado'] == 'Finalizado':
            reportes_finalizados = reportes_filtrados

        context = {
            'reportes_pendientes': reportes_pendientes,
            'reportes_en_proceso': reportes_en_proceso,
            'reportes_finalizados': reportes_finalizados
        }
    else:
        reportes_pendientes = Reporte.objects.filter(estado_reporte='Pendiente').order_by('-id')
        reportes_en_proceso = Reporte.objects.filter(estado_reporte='En proceso')
        reportes_finalizados = Reporte.objects.filter(estado_reporte='Finalizado')
        context = {
            'reportes_pendientes': reportes_pendientes,
            'reportes_en_proceso': reportes_en_proceso,
            'reportes_finalizados': reportes_finalizados
        }
    return render(request, 'reportes_listaV2.html', context)


def actualizar_reporte(request, pk):
    reporte = Reporte.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST['btnradio'])
        print(request.POST['observacion'])
        reporte.observacion = request.POST['observacion']
        reporte.estado_reporte = request.POST['btnradio']
        reporte.save()
        return redirect('/lista_reportes')
    context = {'reporte': reporte}
    return render(request, 'reporte_actualizar.html', context)


def reportes_detalles(request, reporte_number):
    reporte = Reporte(pk=reporte_number)
    usuario_reporte = reporte.usuario_reporte
    sector_reporte = reporte.sector_reporte
    direccion_reporte = reporte.direccion_reporte
    categoria_reporte = reporte.categoria_reporte
    return render(request, "reporte_detalle.html", locals())
