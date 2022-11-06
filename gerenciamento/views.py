from django.shortcuts import render, redirect
from .forms import ParticipanteForm
import random

# Create your views here.


def home(request):
    return render(request, 'gerenciamento/home.html', locals())


def cadastramento(request):
    form = ParticipanteForm()

    if request.method == 'POST':
        print(request.POST)
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            print("aqui")
            form.save()
            return redirect(request, 'gerenciamento/cadastramento.html', locals())

    context = {'form': form}
    return render(request, 'gerenciamento/cadastramento.html', locals())


def listar_participantes(request):
    return render(request, 'gerenciamento/listar_participantes.html', locals())


def registrar_entrada(request):
    return render(request, 'gerenciamento/registrar_entrada.html', locals())


def registrar_saida(request):
    return render(request, 'gerenciamento/registrar_saida.html', locals())
