
"""
DIA: 1
VERSÃO: 1.3
DESCRIÇÃO: Administração de categorias e produtos no MercaSys 2.0.
HISTÓRICO: Mantém a contagem de categorias e adiciona a listagem de produtos.
"""

from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id_categoria",
        "codigo_categoria",
        "nome",
    )

    search_fields = (
        "codigo_categoria",
        "nome",
        "descricao",
    )

    ordering = ("nome",)
    list_per_page = 10

    def changelist_view(self, request, extra_context=None):
        total_categorias = Categoria.objects.count()

        extra_context = extra_context or {}
        extra_context["total_categorias"] = total_categorias

        return super().changelist_view(
            request,
            extra_context=extra_context,
        )


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "id_produto",
        "codigo_produto",
        "nome",
        "id_categoria",
        "id_fornecedor",
        "preco",
        "codigo_barras",
    )

    search_fields = (
        "codigo_produto",
        "nome",
        "codigo_barras",
        "id_categoria__nome",
        "id_fornecedor__nome_fantasia",
    )

    list_filter = (
        "id_categoria",
        "id_fornecedor",
    )

    ordering = ("nome",)
    list_per_page = 10
