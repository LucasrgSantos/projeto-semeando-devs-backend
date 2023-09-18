from django.contrib import admin
from .models import Pessoas, Respostas, Valores

@admin.register(Pessoas)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'dataNascimento', 'uf', 'cidade', 'email', 'telefone')

@admin.register(Respostas)
class RespostasAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome', 'get_cpf', 'resposta1', 'resposta2', 'resposta3', 'resposta4')

    def get_nome(self, obj):
        return obj.pessoa.nome
    
    def get_cpf(self, obj):
        return obj.pessoa.cpf

    get_nome.short_description = 'Nome'
    get_cpf.short_description = 'CPF'

@admin.register(Valores)
class ValoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome', 'get_cpf', 'valorCorrida', 'valorCorridaComDesconto')

    def get_nome(self, obj):
        return obj.pessoa.nome
    
    def get_cpf(self, obj):
        return obj.pessoa.cpf

    get_nome.short_description = 'Nome'
    get_cpf.short_description = 'CPF'
