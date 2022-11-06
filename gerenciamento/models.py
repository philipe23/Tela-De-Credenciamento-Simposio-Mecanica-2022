from django.db import models
import random
import string

# Create your models here.


def generate_codigo(n):
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    codigo = ""
    while n:
        codigo += base[random.randint(1, 1000) % 35]
        n -= 1
    return codigo


class Participante(models.Model):
    primeiro_nome = models.CharField(max_length=255, null=True)
    ultimo_nome = models.CharField(max_length=255, null=True)
    matricula = models.CharField(max_length=255, null=True)
    codigo = models.CharField(max_length=9, default=generate_codigo(8), null=True)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome


class Movimentacao(models.Model):
    participante = models.ForeignKey(Participante, related_name='movimentacao', on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField(auto_now_add=True, null=True)
    horario_saida = models.DateTimeField(null=True)

    def __str__(self):
        return f' {self.participante.primeiro_nome} entrada: {self.horario_entrada} saída: {self.horario_saida} '
