# Checkout Transparente <sub>(em desenvolvimento)</sub>

Este é um projeto que demonstra a implementação completa de um checkout transparente utilizando a API de pagamentos do Asaas.

O objetivo é implementar uma solução de checkout transparente para a venda de um produto, servindo como aprendizado para novas tecnologias e consolidação de coisas que já sei. O sistema permitirá o pagamento (Cartão de Crédito, Boleto ou PIX) diretamente no site próprio, sem redirecionamento, integrando-se à API do Asaas em modo Sandbox para processamento e a um banco de dados para gestão de clientes e pedidos.

---

## Sobre o projeto

O projeto utiliza uma arquitetura monolítica em Python, com o Flask sendo responsável tanto pela lógica de back-end quanto pela renderização das páginas.

O fluxo de compra é dividido em três páginas:

1. **Página de Produto:** Exibe o produto, seletor de quantidade e valor.
2. **Página de Checkout:** Para onde o usuário é levado após adicionar ao carrinho. Exibe o resumo do pedido e o formulário para pagamento.
3. **Página de Pedido Confirmado:** Página de sucesso exibida após um pagamento ser aprovado.

---

## Funcionalidades

* **Múltiplos métodos de pagamento:** Aceita cartão de crédito, boleto e PIX, todos integrados com a API do Asaas.
* **Banco de dados:** Utiliza Postgres para salvar clientes e pedidos, evitando duplicidade e mantendo um histórico das transações.
* **Segurança:** Implementa a tokenização de cartão, garantindo que dados sensíveis nunca passem pelo servidor da aplicação.
* **Modo Sandbox:** Todo o fluxo opera no ambiente de testes do Asaas, permitindo testes seguros sem dinheiro real.

---

## Documentação

A documentação pode ser encontrada na pasta `/docs`

* [Análise de requisitos](./docs/requisitos/)
* [Modelagem do banco de dados](.docs/modelagem/)
