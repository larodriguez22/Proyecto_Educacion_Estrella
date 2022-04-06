from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroFormulario, UsuarioLoginFormulario
from .models import TestUsuario, Pregunta, PreguntasRespondidas


def inicio(request):

    context = {
        'bienvenido': 'Bienvenido'
    }

    return render(request, 'inicio.html', context)


def HomeUsuario(request):

    return(render, 'Usuario/home.html')


def jugar(request):
    Test_usuario, created = TestUsuario.objects.get_or_create(
        usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = Test_usuario.intentos.select_related(
            'pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')
    else:
        
        respondidas = PreguntasRespondidas.objects.filter(
            testUsuario=Test_usuario).values_list('pregunta__pk', flat=True)

        pregunta = Pregunta.objects.exclude(pk__in=respondidas)
        context = {
            'pregunta': pregunta
        }
    return render(request, 'play/jugar.html', context)


def loginView(request):
    titulo = "Login"
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        usuario = authenticate(username=username, password=password)
        login(request, usuario)
        return redirect('/')

    context = {
        'form': form,
        'titulo': titulo
    }
    return render(request, 'Usuario/login.html', context)


def registro(request):
    titulo = 'Crear una cuenta'

    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFormulario()
    context = {
        'form': form,
        'titulo': titulo

    }

    return render(request, 'Usuario/registro.html', context)


def logoutView(request):
    logout(request)
    return redirect('/')
