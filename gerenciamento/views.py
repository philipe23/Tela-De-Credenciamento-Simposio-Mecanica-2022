from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Participante, Movimentacao
from .forms import ParticipanteForm, PresencaForm
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


def listar_participantes_presentes(request):
    participantes = Participante.objects.filter(status='Presente')
    return render(request, 'gerenciamento/listar_participantes_presentes.html', locals())



def registrar_presenca(request):

    form = PresencaForm()
    if request.method == 'POST':
        form = PresencaForm(request.POST)
        if form.is_valid():
            participante = form.cleaned_data['participante']
            codigo = form.cleaned_data['codigo']
            codigo_verificador = participante.codigo
            if codigo != codigo_verificador:
                print('erro')
            else:
                Movimentacao.objects.create(participante=participante)
                print("Presença Registrada!")
            return redirect('home')

    return render(request, 'gerenciamento/registrar_entrada.html', locals())
