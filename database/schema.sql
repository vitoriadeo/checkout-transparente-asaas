DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS produto;

CREATE TABLE produto (
    id_produto SMALLSERIAL PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
    valor_unidade DECIMAL(6,2) NOT NULL,
    descricao VARCHAR(255) NULL
);

CREATE TABLE cliente (
    id_cliente SMALLSERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    cpf_cnpj VARCHAR(18) NOT NULL UNIQUE,
    cep VARCHAR(9) NOT NULL,
    num_residencia VARCHAR(20) NOT NULL,
    id_cliente_asaas VARCHAR(255) NULL
);

CREATE TABLE pedido (
    id_pedido SMALLSERIAL PRIMARY KEY,
    quantidade SMALLINT NOT NULL DEFAULT 1,
    valor_total DECIMAL(7,2) NOT NULL,
    status_pagamento VARCHAR(50) NOT NULL DEFAULT 'pendente',
    data_compra DATE NOT NULL DEFAULT CURRENT_DATE,
    id_pagamento_asaas VARCHAR(255) NULL UNIQUE,
    id_cliente SMALLINT NOT NULL REFERENCES cliente(id_cliente),
    id_produto SMALLINT NOT NULL REFERENCES produto(id_produto)
);