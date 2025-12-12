# 🎲 Jogo: Adivinhe o Número (1 a 100)

## 🎯 Descrição do Projeto
Este é um projeto simples, focado em lógica e controle de fluxo, onde o objetivo é que o usuário adivinhe um número secreto gerado aleatoriamente pelo computador. O sistema fornece dicas ("MAIOR" ou "MENOR") após cada tentativa.

## 💻 Conceitos de Programação Aplicados

O projeto utiliza os seguintes fundamentos de Python:

* **Módulo `random`:** Uso da função `randint(1, 100)` para gerar o número secreto uma única vez.
* **Controle de Fluxo:** Utilização de `while True` para criar um *loop* de jogo que só termina após o acerto.
* **Condicionais Avançadas:** Uso de `if`, `elif` e `else` para fornecer *feedback* ("MAIOR", "MENOR" ou "ACERTOU").
* **Tratamento de Exceções:** Implementação de `try` e `except ValueError` para garantir que o programa não quebre se o usuário digitar texto em vez de números.
* **Contador:** Variável `tentativas` incrementada (`+= 1`) para rastrear a eficiência do usuário.
* **Funções Básicas:** Uso da função `linhas()` para organização visual do *output*.
