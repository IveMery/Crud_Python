from django.shortcuts import render

from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)

def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    return render(request, 'lista_laboratorios.html', {'laboratorios': laboratorios , 'visit_count': visit_count})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'crear_laboratorio.html', {'form': form})

def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form})


def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('lista_laboratorios')

    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})