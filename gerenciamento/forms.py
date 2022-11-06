from django import forms
from .models import Participante, Movimentacao


class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = ('primeiro_nome', 'ultimo_nome', 'matricula')


class PresencaForm(forms.Form):
    participante = forms.ModelChoiceField(label='Participante', required=True, queryset=Participante.objects.all())
    codigo = forms.CharField(label='Código Verificador', required=True)
