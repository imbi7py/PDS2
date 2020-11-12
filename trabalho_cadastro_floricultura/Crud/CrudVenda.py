# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc, case, func, distinct

from Crud.ConectorDB import Conexao
from Crud.Models import Venda, Cliente, FormaPagamento

class CrudVenda(object):
    def __init__(self, id="", idCliente="", nomeCliente="", sobrenomeCliente="",
                 tipoPagamento="", dataVenda="",
                 subtotal="", desconto="", totalValor="", query=""):
        self.id = id
        self.idCliente = idCliente
        self.nomeCliente = nomeCliente
        self.sobrenomeCliente = sobrenomeCliente
        self.tipoPagamento = tipoPagamento
        self.dataVenda = dataVenda
        self.subtotal = subtotal
        self.desconto = desconto
        self.totalValor = totalValor
        self.query = query

    # Recebendo ultimo Id inserido
    def lastIdVenda(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            ultimo = sessao.query(Venda.id).order_by(
                desc(Venda.id)).limit(1).first()
            self.id = ultimo.id + 1
            sessao.close()
        except:
            self.id = 1
        return self.id

    # Inserir Venda
    def addVenda(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            row = Venda(
                id=self.id,
                idCliente=self.idCliente,
                dataVenda=self.dataVenda,
                tipoPagamento=self.tipoPagamento,
                subtotal=self.subtotal,
                desconto=self.desconto,
            )
            # Add Query na Sessao
            sessao.add(row)
            # Executando a Query
            sessao.commit()
            sessao.close()
        except IntegrityError as err:
            print("Erro: " + err)

    # Listar Venda por ID
    def DetalhamentoVendaId(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            busca = (sessao.query(Venda).get(self.id))
            self.id = busca.id
            self.dataVenda = datetime.strftime(busca.dataVenda, "%d/%m/%Y %H:%M:%S")
            self.tipoPagamento = busca.tipoPagamento
            self.idCliente = busca.idCliente
            self.desconto = busca.desconto
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Listar Vendas
    def listaVenda(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = (sessao.query(Venda.id,
                                       Venda.dataVenda,
                                       FormaPagamento.forma_pagamento,
                                       Venda.subtotal,
                                       Venda.desconto,
                                       Cliente.nome,
                                       Cliente.sobrenome,
                                       Cliente.id.label("idCliente"))
                          .join(Cliente)
                          .join(FormaPagamento)
                          .order_by(Venda.id)
                          )

            # Convertendo variaveis em lista
            self.id = []
            self.dataVenda = []
            self.tipoPagamento = []
            self.valorTotal = []
            self.nomeCliente = []
            self.sobrenomeCliente = []
            self.idCliente = []
            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.dataVenda.append(datetime.strftime(row.dataVenda, "%d/%m/%Y %H:%M:%S"))
                self.tipoPagamento.append(row.forma_pagamento.upper())
                self.valorTotal.append(float(row.subtotal) - float(row.desconto))
                self.nomeCliente.append(row.nome.upper())
                self.sobrenomeCliente.append(row.sobrenome.upper())
                self.idCliente.append(row.idCliente)
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Relatório Vendas por periodo
    def relatValorDia(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            row = (sessao.query(func.COALESCE(
                func.SUM(Venda.subtotal), 0).label('vendido'),
                func.COUNT(distinct(Venda.idCliente)).label('cliente'))
                .filter(Venda.dataVenda.between(self.dataVenda, self.dataVenda)))
            row.all()
            # salvando resultado
            for query in row:
                self.valorTotal = str(query.vendido).replace('.', ',')
                self.idCliente = query.cliente
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)
