# Modelo Lógico

---

**Projeto:** MercaSys 2.0

**Versão:** 1.0

**Status:** Em desenvolvimento

**Data de criação:** 06/08/2026

**Responsável:** Alef Viana Barroso

---
| Tabela      | Chave Primária     |
| ----------- | ------------------ |
| PRODUTO     | **id_produto**     |
| CATEGORIA   | **id_categoria**   |
| FORNECEDOR  | **id_fornecedor**  |
| CLIENTE     | **id_cliente**     |
| FUNCIONARIO | **id_funcionario** |
| VENDA       | **id_venda**       |
| ITEM_VENDA  | **id_item_venda**  |
| PAGAMENTO   | **id_pagamento**   |
| ESTOQUE     | **id_estoque**     |
| CAIXA       | **id_caixa**       |

---
PRODUTO
-------------------------
PK  id_produto              INTEGER
FK  id_categoria            INTEGER
FK  id_fornecedor           INTEGER
    codigo_produto          VARCHAR
    nome                    VARCHAR
    descricao               TEXT
    preco                   NUMERIC
    codigo_barras           VARCHAR
---
CATEGORIA
-------------------------
PK  id_categoria            INTEGER
    codigo_categoria        VARCHAR
    nome                    VARCHAR
    descricao               TEXT
---
FORNECEDOR
-------------------------
PK  id_fornecedor           INTEGER
    razao_social            VARCHAR
    nome_fantasia           VARCHAR
    cnpj                    VARCHAR
    telefone                VARCHAR
    email                   VARCHAR
    endereco                VARCHAR
---
CLIENTE
-------------------------
PK  id_cliente              INTEGER
    nome                    VARCHAR
    cpf                     VARCHAR
    telefone                VARCHAR
    email                   VARCHAR
---
FUNCIONARIO
-------------------------
PK  id_funcionario          INTEGER
    nome                    VARCHAR
    cpf                     VARCHAR
    telefone                VARCHAR
    email                   VARCHAR
    cargo                   VARCHAR
    status                  VARCHAR
---
VENDA
-------------------------
PK  id_venda                INTEGER
FK  id_cliente              INTEGER
FK  id_funcionario          INTEGER
FK  id_caixa                INTEGER
    data_venda              DATE
    hora_venda              TIME
    valor_total             NUMERIC
    status                  VARCHAR
---
ITEM_VENDA
-------------------------
PK  id_item_venda           INTEGER
FK  id_produto              INTEGER
FK  id_venda                INTEGER
    quantidade              INTEGER
    preco_unitario          NUMERIC
    subtotal                NUMERIC
---
PAGAMENTO
-------------------------
PK  id_pagamento            INTEGER
FK  id_venda                INTEGER
    forma_pagamento         VARCHAR
    valor                   NUMERIC
    data_pagamento          DATE
    status                  VARCHAR
---
ESTOQUE
-------------------------
PK  id_estoque              INTEGER
FK  id_produto              INTEGER
    quantidade_galpao       INTEGER
    quantidade_prateleira   INTEGER
    entradas                INTEGER
    saidas                  INTEGER
---
CAIXA
-------------------------
PK  id_caixa                INTEGER
    numero_caixa            INTEGER
    status                  VARCHAR
---

## Objetivo

Transformar o DER Conceitual em um modelo lógico de banco de dados, definindo tabelas, chaves primárias, chaves estrangeiras e atributos que serão implementados no PostgreSQL.

---