from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Participante
from .forms import ParticipanteForm, EntradaForm
import random

# Create your views here.


def home(request):
    return render(request, 'gerenciamento/home.html', locals())


def cadastramento(request):
    form = ParticipanteForm()

    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'gerenciamento/cadastramento.html', locals())


def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'gerenciamento/listar_participantes.html', locals())


def registrar_entrada(request):
    form = EntradaForm()

    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'gerenciamento/registrar_entrada.html', locals())


def registrar_saida(request):
    return render(request, 'gerenciamento/registrar_saida.html', locals())
