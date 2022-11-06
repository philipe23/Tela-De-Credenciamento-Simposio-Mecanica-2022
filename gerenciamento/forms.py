from django import forms
from .models import Participante, Movimentacao



class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = ('primeiro_nome', 'ultimo_nome', 'matricula')


class EntradaForm(forms.Form):
    participante = forms.ModelChoiceField(label='Participante', required=True, queryset=Participante.objects.all())
    codigo = forms.CharField(label='Código Verificador', required=True)

    def save(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
