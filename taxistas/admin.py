from django.contrib import admin

from .models import Taxista

@admin.register(Taxista)
class TaxistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'numero')
