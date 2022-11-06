from django import forms
from .models import Participante, Movimentacao


class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = ('primeiro_nome', 'ultimo_nome', 'matricula')


class EntradaForm(forms.ModelForm):

    class Meta:
        model = Movimentacao
        fields = ('participante', 'horario_entrada')
