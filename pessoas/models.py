from django.db import models

class Pessoas(models.Model):

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    dataNascimento = models.CharField(max_length=10)
    uf = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=16)  

class Respostas(models.Model):

    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    resposta1 = models.CharField(max_length=255)
    resposta2 = models.CharField(max_length=255)
    resposta3 = models.CharField(max_length=255)
    resposta4 = models.CharField(max_length=255)

class Valores(models.Model):

    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    valorCorrida = models.CharField(max_length=10)
    valorCorridaComDesconto = models.CharField(max_length=10)

