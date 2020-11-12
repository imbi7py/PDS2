# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from Crud.ConectorDB import Conexao
from Crud.Models import CategoriaProduto

class CrudCategoriaProduto(object):
    def __init__(self, id="", categoria_produto="", query=""):
        self.id = id
        self.categoria_produto = categoria_produto
        self.query = query

    # Listando todas as categorias
    def listaCategoriaProduto(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            self.query = (sessao.query(CategoriaProduto)
                            .order_by(CategoriaProduto.categoria_produto).all())
            # Convertendo variaveis em lista
            self.id = []
            self.categoria_produto = []
            for row in self.query:
                self.id.append(row.id)
                self.categoria_produto.append(row.categoria_produto.upper())
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)