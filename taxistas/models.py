from django.db import models

class Taxista(models.Model):

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    numero = models.CharField(max_length=4)

    @classmethod
    def validar_numero_taxista(cls, numero_taxista):
        try:
            taxista = cls.objects.get(numero=numero_taxista)
            return True
        except cls.DoesNotExist:
            return False 