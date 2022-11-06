from django.db import models

# Create your models here.


class Participante(models.Model):
    primeiro_nome = models.CharField(max_length=255, null=True),
    ultimo_nome = models.CharField(max_length=255, null=True)
    matricula = models.CharField(max_length=255, null=True)
    codigo = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.primeiro_nome + ' ' + self.ultimo_nome


class Entrada(models.Model):
    participante = models.ManyToManyField(Participante, on_delete=models.CASCADE)
    horario = models.DateTimeField(auto_now=True)

class Saida(models.Model):
    participante = models.ManyToManyField(Participante, on_delete=models.CASCADE)
    horario = models.DateTimeField(auto_now=True)
    