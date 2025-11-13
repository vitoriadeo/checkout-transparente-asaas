import os, logging
import pyodbc
from app.config import Config

logger = logging.getLogger(__name__)
conn_str = Config.pyodbc_conn
conn = None
cur = None
print(f"DEBUG: String de Conexão Sendo Usada:\n>>> {conn_str} <<<")

try:
    logger.info("Conectando aos AWS RDS/SQL Server...")
    conn = pyodbc.connect(conn_str, autocommit=True)
    logger.info("Conexão estabelecida!")

    cur = conn.cursor()

    logger.info("Executando scripts de criação de tabelas...")

    create_table_produto = """
        create table produto (
        id_produto tinyint primary key identity,
        nome_produto nvarchar(255) not null,
        valor_unidade decimal(6,2) not null,
        descricao nvarchar(255) null
        )
    """
    logger.info("Criando tabela PRODUTO...")
    cur.execute(create_table_produto)

    create_table_cliente = """
        create table cliente (
        id_cliente smallint primary key identity,
        nome nvarchar(255) not null,
        email nvarchar(255) not null unique,
        cpf_cnpj varchar(18) not null unique,
        cep varchar(9) not null,
        num_residencia nvarchar(20) not null,
        id_cliente_asaas nvarchar(255) null)
    """
    logger.info("Criando tabela CLIENTE...")
    cur.execute(create_table_cliente)

    create_table_pedido = """
        create table pedido (
        id_pedido smallint primary key identity,
        quantidade tinyint not null default 1,
        valor_total decimal(7,2) not null,
        status_pagamento nvarchar(50) not null default 'pendente',
        data_compra date not null default current_date(),
        id_pagamento_asaas varchar(255) null unique,
        id_cliente smallint not null references cliente(id_cliente),
        id_produto tinyint not null references produto(id_produto))
    """
    logger.info("Criando tabela PEDIDO...")
    cur.execute(create_table_pedido)

    logger.info("Tabelas criadas com sucesso!")

except pyodbc.OperationalError as e:
    logger.error(f"Erro de conexão: {e}")
    raise e

except Exception as e:
    logger.error(f"Falha na iniciallização do banco: {e}")
    raise e

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
        logger.info("Conexão com RDS fechada.")