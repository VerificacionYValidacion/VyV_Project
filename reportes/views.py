from django.shortcuts import render
from .forms import ReporteForm
# Create your views here.
from .models import Reporte


def index(request):
    form_class = ReporteForm()
    if request.method == 'POST':
        form_class = ReporteForm(request.POST, request.FILES)
        if form_class.is_valid():
            form_class.save()
        else:
            print("Form no valido")

    context = {'form': form_class}
    return render(request, 'reporte_modelform.html', context)


def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'reportes_lista.html', {
        'reportes': reportes
    })
