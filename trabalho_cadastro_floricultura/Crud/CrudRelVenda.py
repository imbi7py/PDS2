# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import case

from Crud.ConectorDB import Conexao
from Crud.Models import RelacaoVenda, Produto


class CrudRelVenda(object):
    def __init__(self, id="", idVenda="", idProduto="",
                 produto="", qtd="", valorUnitario="", valorTotal="",
                 query=""):
        self.id = id
        self.idVenda = idVenda
        self.idProduto = idProduto
        self.produto = produto
        self.qtd = qtd
        self.valorUnitario = valorUnitario
        self.valorTotal = valorTotal
        self.query = query

    # Cadastrando item referente a Venda
    def addItens(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            row = RelacaoVenda(
                idVenda=self.idVenda,
                idProduto=self.idProduto,
                qtd=self.qtd,
                valorUnitario=self.valorUnitario,
                valorTotal=self.valorTotal,
            )
            # Adicionando query na sessao
            sessao.add(row)
            sessao.commit()
            sessao.close()
        except IntegrityError:
            self.updateItensVenda()

    # Lista Itens por id de Venda
    def listaItens(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = (sessao.query(
                RelacaoVenda.id,
                RelacaoVenda.idVenda,
                RelacaoVenda.idProduto,
                RelacaoVenda.qtd,
                RelacaoVenda.valorUnitario,
                RelacaoVenda.valorTotal,
                Produto.produto)
                .join(Produto)
                .filter(RelacaoVenda.idVenda == self.idVenda))
            self.query.all()
            # Convertendo variaveis em lista
            self.id = []
            self.idVenda = []
            self.idProduto = []
            self.produto = []
            self.qtd = []
            self.valorUnitario = []
            self.valorTotal = []

            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.idVenda.append(row.idVenda)
                self.idProduto.append(row.idProduto)
                self.produto.append(row.produto)
                self.qtd.append(row.qtd)
                self.valorUnitario.append(row.valorUnitario)
                self.valorTotal.append(row.valorTotal)
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Deletando item
    def deletaItem(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Selecionando ID
            self.query = (sessao.query(RelacaoVenda).get(self.id))
            if self.query:
                # add query na sessao
                sessao.delete(self.query)
                sessao.commit()
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)
