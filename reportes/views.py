from django.shortcuts import render

import reportes.models
from .forms import ReporteForm
from .models import Reporte
from django.contrib import messages


def index(request):
    form_class = ReporteForm()
    reporte = Reporte()
    if request.method == 'POST':
        form_class = ReporteForm(request.POST, request.FILES)
        if form_class.is_valid():
            form_class.save()
            messages.success(request, reporte.notificar_reporte_enviado())
        else:
            print("Form no valido")

    context = {'form': form_class}
    return render(request, 'reporte_modelform.html', context)


def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'reportes_lista.html', {
        'reportes': reportes
    })
