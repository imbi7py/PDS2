# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from Crud.ConectorDB import Conexao
from Crud.Models import FormaPagamento

class CrudFormaPagamento(object):
    def __init__(self, id="", formaPagamento="", query=""):
        self.id = id
        self.formaPagamento = formaPagamento
        self.query = query

    # Listando todas as categorias
    def listaFormaPagamento(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = (sessao.query(FormaPagamento)
                            .order_by(FormaPagamento.forma_pagamento).all())
            # Convertendo variaveis em lista
            self.id = []
            self.formaPagamento = []
            for row in self.query:
                self.id.append(row.id)
                self.formaPagamento.append(row.forma_pagamento.upper())
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)
