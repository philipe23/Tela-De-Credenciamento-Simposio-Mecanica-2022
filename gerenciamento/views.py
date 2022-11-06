from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'gerenciamento/home.html', locals())


def cadastramento(request):
    return render(request, 'gerenciamento/cadastramento.html', locals())


def listar_participantes(request):
    return render(request, 'gerenciamento/listar_participantes.html', locals())


def registrar_entrada(request):
    return render(request, 'gerenciamento/registrar_entrada.html', locals())


def registrar_saida(request):
    return render(request, 'gerenciamento/registrar_saida.html', locals())
