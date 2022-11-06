from django.contrib import admin
from .models import Participante, Movimentacao

# Register your models here.


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['primeiro_nome', 'ultimo_nome', 'matricula']
    search_fields = ('primeiro_nome', 'ultimo_nome', 'matricula')


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ['participante', 'status', 'horario_entrada', 'horario_saida']
    search_fields = ('participante',)
    list_filter = ['status']
