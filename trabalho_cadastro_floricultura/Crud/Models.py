# coding=utf-8

from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.dialects.mysql import LONGBLOB

from Crud.ConectorDB import Base

# tabela Cliente
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(40), index=True, nullable=False)
    sobrenome = Column(String(40), nullable=False)
    cpf = Column(String(15), nullable=False)
    rg = Column(String(15), nullable=False)
    celular = Column(String(15))
    telefone = Column(String(15))
    email = Column(String(50), nullable=False)
    obs = Column(String(100))
    cep = Column(String(12))
    endereco = Column(String(40))
    numero = Column(String(5))
    bairro = Column(String(40))
    cidade = Column(String(40))
    estado = Column(String(2))

    def __repr__(self):
        return self.nome

# Tabela Categoria de produtos
class CategoriaProduto(Base):
    __tablename__ = 'categoria_produto'
    id = Column(Integer, primary_key=True, nullable=False)
    categoria_produto = Column(String(50), index=True, nullable=False)

    def __repr__(self):
        return self.categoria_produto

# Tabela Marca Produtos
class MarcaProduto(Base):
    __tablename__ = 'marca_produto'
    id = Column(Integer, primary_key=True, nullable=False)
    marca_produto = Column(String(50), index=True, nullable=False)

    def __repr__(self):
        return self.marca_produto

# Tabela Produtos
class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, nullable=False)
    produto = Column(String(80), index=True, nullable=False)
    descricao = Column(String(120), index=True)
    imagem = Column(LONGBLOB(length=None))
    categoria = Column(Integer, ForeignKey('categoria_produto.id'), nullable=False)
    marca = Column(Integer, ForeignKey('marca_produto.id'), nullable=False)
    qtdMinimoEstoque = Column(Integer, default=0, nullable=False)
    qtdEstoque = Column(Integer, default=0, nullable=False)
    valorUnitario = Column(Numeric(9, 2), default='0.00', nullable=False)

    def __repr__(self):
        return self.produto

# Tabela Forma de Pagamento
class FormaPagamento(Base):
    __tablename__ = 'forma_de_pagamento'
    id = Column(Integer, primary_key=True, nullable=False)
    forma_pagamento = Column(String(50), index=True, nullable=False)

    def __repr__(self):
        return self.forma_pagamento

# Tabela Vendas
class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    idCliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    tipoPagamento = Column(Integer, ForeignKey('forma_de_pagamento.id'), default=1, nullable=False)
    dataVenda = Column(DateTime, nullable=False)
    subtotal = Column(Numeric(9, 2), default='0.00', nullable=False)
    desconto = Column(Numeric(9, 2), default='0.00')

    def __repr__(self):
        return self.id

# Tabela relação de item comprados (carrinho de compra)
class RelacaoVenda(Base):
    __tablename__ = 'relacao_venda'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    idVenda = Column(Integer, ForeignKey('venda.id'), nullable=False)
    idProduto = Column(Integer, ForeignKey('produto.id'), nullable=False)
    qtd = Column(Numeric(9, 2), default='0.00', nullable=False)
    valorUnitario = Column(Numeric(9, 2), default='0.00', nullable=False)
    valorTotal = Column(Numeric(9, 2), default='0.00', nullable=False)

    def __repr__(self):
        return self.id
