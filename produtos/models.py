
"""
DIA: 1
VERSÃO: 1.0
DESCRIÇÃO: Modelo de categorias do MercaSys 2.0
HISTÓRICO: Criação inicial do modelo Categoria.
"""

from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    codigo_categoria = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)

    id_categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        db_column="id_categoria",
        related_name="produtos",
    )

    id_fornecedor = models.ForeignKey(
        "fornecedores.Fornecedor",
        on_delete=models.PROTECT,
        db_column="id_fornecedor",
        related_name="produtos",
    )

    codigo_produto = models.CharField(max_length=50)
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
