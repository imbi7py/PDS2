# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from Crud.ConectorDB import Conexao
from Crud.Models import MarcaProduto

class CrudMarcaProduto(object):
    def __init__(self, id="", marca_produto="", query=""):
        self.id = id
        self.marca_produto = marca_produto
        self.query = query

    # Listando todas as Marcas
    def ListaMarcaProdutos(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            self.query = (sessao.query(MarcaProduto)
                            .order_by(MarcaProduto.marca_produto).all())

            # Convertendo variaveis em lista
            self.id = []
            self.marca_produto = []
            # salvando resultado em sua lista
            for row in self.query:
                self.id.append(row.id)
                self.marca_produto.append(row.marca_produto.upper())
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

