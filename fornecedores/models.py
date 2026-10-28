from django.db import models


class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_fantasia