# Checkout Transparente com Asaas <sub>(em desenvolvimento)</sub>

Este é um projeto de portfólio que demonstra a implementação completa de um **checkout transparente** utilizando a API de pagamentos do Asaas.

O objetivo é simular a venda de um produto único, onde o usuário insere seus dados pessoais e os dados para pagamento diretamente na página, sem ser redirecionado para um ambiente externo. O projeto é dividido em duas partes:

1.  Uma página HTML simples que captura os dados e se comunica com a biblioteca do Asaas para tokenizar o cartão ou gerar outra forma de pagamento.
2.  Um servidor em Python/Flask que recebe os dados, gerencia clientes e pedidos em um banco de dados e processa o pagamento de forma segura junto à API do Asaas.

---

## Funcionalidades
* **Múltiplos métodos de pagamento:** Aceita cartão de crédito (via checkout transparente), boleto e PIX, todos integrados com a API do Asaas.
* **Banco de dados próprio:** Utiliza Postgres (Supabase) para salvar clientes e pedidos, evitando duplicidade e mantendo um histórico das transações.
* **Arquitetura desacoplada:** A API (back-end em Python/Flask) é totalmente independente do site (front-end em HTML/JS), comunicando-se via JSON.
* **Segurança:** Implementa a tokenização de cartão, garantindo que dados sensíveis nunca passem pelo servidor da aplicação.
* **Modo Sandbox:** Todo o fluxo opera no ambiente de testes do Asaas, permitindo testes seguros sem dinheiro real.

---

## Documentação
A documentação pode ser encontrada na pasta `/docs`
- Análise de requisitos
- Modelagem do banco de dados

---
