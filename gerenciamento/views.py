from django.shortcuts import render, redirect
from .models import Participante, Movimentacao, ConfirmarEntrada
from .forms import ParticipanteForm, PresencaForm

# Create your views here.


def home(request):
    return render(request, 'gerenciamento/home.html', locals())


def cadastramento(request):
    form = ParticipanteForm()

    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            primeiro_nome = form.cleaned_data['primeiro_nome']
            ultimo_nome = form.cleaned_data['ultimo_nome']
            matricula = form.cleaned_data['matricula']
            Participante.objects.create(
                primeiro_nome=primeiro_nome, ultimo_nome=ultimo_nome, matricula=matricula
            )
            return redirect('home')

    return render(request, 'gerenciamento/cadastramento.html', locals())


def confirmar_entrada(request, pk):
    participante = Participante.objects.get(id=pk)
    participante.status = '1'
    participante.save(update_fields=['status'])
    ConfirmarEntrada.objects.create(participante=participante)

    return redirect('listar_participantes')


def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'gerenciamento/listar_participantes.html', locals())


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
