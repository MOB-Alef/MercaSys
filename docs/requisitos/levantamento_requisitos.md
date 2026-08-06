# Levantamento de Requisitos

---

**Projeto:** MercaSys 2.0

**Versão:** 2.0

**Status:** Em desenvolvimento

**Data de criação:** 05/08/2026

**Responsável:** Alef Viana Barroso

---

## Objetivo

Desenvolver um sistema web para gerenciamento de mercados, permitindo controlar produtos, estoque, vendas, funcionários e relatórios, oferecendo uma plataforma organizada, segura e preparada para crescer.

---

## Descrição do Projeto

O MercaSys é um sistema web desenvolvido para auxiliar no gerenciamento de pequenos e médios mercados. Seu objetivo é informatizar processos que normalmente são realizados de forma manual, oferecendo maior organização, segurança e agilidade nas operações diárias.

O sistema permitirá controlar produtos, estoque, vendas, funcionários, clientes, fornecedores e relatórios gerenciais, reunindo todas as informações em uma única plataforma.

---

## Problema

Muitos pequenos mercados ainda utilizam processos manuais ou planilhas para controlar suas operações.

Essa forma de gerenciamento pode causar:

- Perda de informações;
- Erros no controle de estoque;
- Demora no atendimento;
- Dificuldade para localizar produtos;
- Falta de relatórios confiáveis;
- Baixo controle financeiro;
- Dificuldade para acompanhar o desempenho do mercado.

O MercaSys foi idealizado para reduzir esses problemas por meio de um sistema integrado de gerenciamento.

---

## Solução Proposta

Desenvolver um sistema web utilizando Django e PostgreSQL capaz de integrar todos os setores do mercado em uma única plataforma.

O sistema será dividido em módulos independentes, permitindo controlar:

- Produtos;
- Categorias;
- Estoque;
- Funcionários;
- Clientes;
- Fornecedores;
- Caixa (PDV);
- Vendas;
- Relatórios;
- Administração do sistema.

Cada usuário terá permissões específicas de acordo com sua função dentro do mercado, garantindo maior segurança e organização das informações.

---
## Perfis de Usuários

O sistema contará com diferentes níveis de acesso para garantir segurança e organização das operações.

### Administrador

Possui acesso total ao sistema, podendo cadastrar, alterar e remover qualquer informação, além de gerenciar usuários e permissões.

### Supervisor

Pode acompanhar as operações do mercado por meio de consultas e relatórios, sem alterar informações críticas.

### Gerente

Responsável pela administração da loja, podendo gerenciar produtos, estoque, funcionários e acompanhar o desempenho das vendas.

### Operador de Caixa

Responsável pelo atendimento ao cliente, registro das vendas, abertura e fechamento de caixa e recebimento de pagamentos.

---

## Funcionamento Geral

O sistema iniciará com o cadastro das informações básicas do mercado, como produtos, categorias, fornecedores e funcionários.

Após essa configuração inicial, os operadores de caixa poderão registrar vendas normalmente, enquanto os demais usuários acompanharão as operações de acordo com suas permissões.

Todas as movimentações realizadas refletirão automaticamente nos relatórios e no controle de estoque.

---

## Módulos do Sistema

O MercaSys será dividido nos seguintes módulos:

- Login
- Dashboard
- Produtos
- Categorias
- Estoque
- Clientes
- Funcionários
- Fornecedores
- Caixa (PDV)
- Vendas
- Relatórios
- Administração
Cada módulo será desenvolvido de forma independente, permitindo que o sistema evolua de maneira organizada, facilitando futuras manutenções e a inclusão de novas funcionalidades sem comprometer os demais componentes.

---

## Considerações Finais

O levantamento de requisitos representa a primeira etapa do desenvolvimento do MercaSys 2.0.

As informações documentadas neste capítulo servirão como base para a modelagem do banco de dados, definição das regras de negócio e desenvolvimento do sistema web.

---