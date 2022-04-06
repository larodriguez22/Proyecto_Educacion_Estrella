from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import RegistroFormulario


def inicio(request):

    context = {
        'bienvenido': 'Bienvenido'
    }

    return render(request, 'inicio.html', context)


def registro(request):
    titulo = 'Crear una cuenta'

    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = RegistroFormulario()
    context = {
        'form': form,
        'titulo': titulo

    }

    return render(request, 'Usuario/registro.html', context)
