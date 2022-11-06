from django import forms
from .models import Participante


class ParticipanteForm(forms.Form):
    primeiro_nome = forms.CharField(label='Primeiro Nome', required=True, max_length=255)
    ultimo_nome = forms.CharField(label='Sobrenome', required=True, max_length=255)
    matricula = forms.CharField(label='Matrícula', required=True, max_length=255)


class PresencaForm(forms.Form):
    participante = forms.ModelChoiceField(label='Participante', required=True, queryset=Participante.objects.all())
    codigo = forms.CharField(label='Código Verificador', required=True)
