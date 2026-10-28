
"""
DIA: 1
VERSÃO: 1.0
DESCRIÇÃO: Registro de fornecedores no Django Admin.
HISTÓRICO: Configuração inicial da listagem de fornecedores.
"""

from django.contrib import admin
from .models import Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = (
        "id_fornecedor",
        "cnpj",
        "razao_social",
        "nome_fantasia",
        "telefone",
    )

    search_fields = (
        "cnpj",
        "razao_social",
        "nome_fantasia",
    )

    ordering = ("nome_fantasia",)
    list_per_page = 10
