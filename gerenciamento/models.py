from django.db import models
import random
import string

# Create your models here.


def get_random_string(length):
    result = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result


class Participante(models.Model):
    primeiro_nome = models.CharField(max_length=255, null=True)
    ultimo_nome = models.CharField(max_length=255, null=True)
    matricula = models.CharField(max_length=255, null=True)
    codigo = models.CharField(max_length=8, default=get_random_string(6), null=True)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome


class Movimentacao(models.Model):
    participante = models.ForeignKey(Participante, related_name='movimentacao', on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField(auto_now=True)
    horario_saida = models.DateTimeField(auto_now=True)
