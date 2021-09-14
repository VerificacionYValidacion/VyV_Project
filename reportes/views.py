from django.shortcuts import render, redirect

from cuentas.models import Usuario
from .forms import ReporteForm
from .models import Reporte, Estado
from django.contrib import messages
from django.views.generic import UpdateView


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
    reportes = Reporte.objects.all()
    return render(request, 'reportes_lista.html', {
        'reportes': reportes
    })


def actualizar_reporte(request, pk):
    reporte = Reporte.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST['btnradio'])
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
