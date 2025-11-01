# Checkout Transparente com Asaas <sub>(em desenvolvimento)</sub>

Este é um projeto que demonstra a implementação completa de um **checkout transparente** utilizando a API de pagamentos do Asaas.

O objetivo é implementar uma solução de checkout transparente para a venda de um produto (simulado), servindo como aprendizado. O sistema permitirá o pagamento (Cartão de Crédito, Boleto ou PIX) diretamente no site próprio, sem redirecionamento, integrando-se à API do Asaas (em modo Sandbox) para processamento e a um banco de dados (Supabase/Postgres) para gestão de clientes e pedidos.

---

## Arquitetura e Fluxo do Usuário

O projeto utiliza uma arquitetura **monolítica** em Python, com o **Flask** sendo responsável tanto pela lógica de back-end quanto pela renderização das páginas (server-side) utilizando **Jinja2**.

O fluxo de compra é dividido em três páginas:

1. **Página de Produto:** Exibe o produto, seletor de quantidade e valor.
2. **Página de Checkout:** Para onde o usuário é levado após adicionar ao carrinho. Exibe o resumo do pedido e o formulário para pagamento.
3. **Página de Pedido Confirmado:** Página de sucesso exibida após um pagamento (com Cartão de Crédito) ser aprovado.

---

## Funcionalidades

* **Múltiplos métodos de pagamento:** Aceita cartão de crédito (via checkout transparente), boleto e PIX, todos integrados com a API do Asaas.
* **Banco de dados próprio:** Utiliza Postgres (Supabase) para salvar clientes e pedidos, evitando duplicidade e mantendo um histórico das transações.
* **Arquitetura Monolítica:** A aplicação (back-end em Python/Flask) renderiza o front-end (HTML/Jinja2), simplificando o fluxo de dados e a gestão do estado do usuário (carrinho) via sessão.
* **Segurança:** Implementa a tokenização de cartão, garantindo que dados sensíveis nunca passem pelo servidor da aplicação.
* **Modo Sandbox:** Todo o fluxo opera no ambiente de testes do Asaas, permitindo testes seguros sem dinheiro real.

---

## Documentação

A documentação pode ser encontrada na pasta `/docs`

* [Análise de requisitos](./docs/requisitos/Documento%20de%20Requisitos.pdf)
* Modelagem do banco de dados
