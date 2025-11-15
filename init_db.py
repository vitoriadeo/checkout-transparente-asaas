import os, logging
import psycopg2
from app.config import Config

logger = logging.getLogger(__name__)
conn_str = Config.DB_URL
conn = None
cur = None

try:
    logger.info("Conectando aos AWS RDS/PostgreSQL...")
    conn = psycopg2.connect(conn_str)
    logger.info("Conexão estabelecida!")

    cur = conn.cursor()

    logger.info("Executando scripts de criação de tabelas...")

    create_table_produto = """
        create table produto (
        id_produto smallserial primary key,
        nome_produto varchar(255) not null,
        valor_unidade decimal(6,2) not null,
        descricao varchar(255) null
        )
    """
    logger.info("Criando tabela PRODUTO...")
    cur.execute(create_table_produto)

    create_table_cliente = """
        create table cliente (
        id_cliente smallserial primary key,
        nome varchar(255) not null,
        email varchar(255) not null unique,
        cpf_cnpj varchar(18) not null unique,
        cep varchar(9) not null,
        num_residencia varchar(20) not null,
        id_cliente_asaas varchar(255) null)
    """
    logger.info("Criando tabela CLIENTE...")
    cur.execute(create_table_cliente)

    create_table_pedido = """
        create table pedido (
        id_pedido smallserial primary key,
        quantidade smallint not null default 1,
        valor_total decimal(7,2) not null,
        status_pagamento varchar(50) not null default 'pendente',
        data_compra date not null default current_date,
        id_pagamento_asaas varchar(255) null unique,
        id_cliente smallint not null references cliente(id_cliente),
        id_produto smallint not null references produto(id_produto))
    """
    logger.info("Criando tabela PEDIDO...")
    cur.execute(create_table_pedido)

    conn.commit()
    logger.info("Tabelas criadas com sucesso!")

except psycopg2.OperationalError as e:
    logger.error(f"Erro de conexão: {e}")
    conn.rollback()
    logger.warning(">> Desfazendo transação")
    raise e

except Exception as e:
    logger.error(f"Falha na iniciallização do banco: {e}")
    conn.rollback()
    logger.warning(">> Desfazendo transação")
    raise e

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
        logger.info("Conexão com RDS fechada.")