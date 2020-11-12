# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from sqlalchemy import func

from Crud.ConectorDB import Conexao
from Crud.Models import Produto, CategoriaProduto, MarcaProduto

class CrudProduto(object):
    def __init__(self, id="", produto="", descricao="",
                 imagem="", categoria="", marca="",
                 qtdMinimoEstoque="", qtdEstoque="", qtdAlterarEstoque="",
                 valorUnitario="", totalEstoque="", query=""):
        self.id = id
        self.produto = produto
        self.descricao = descricao
        self.imagem = imagem
        self.categoria = categoria
        self.marca = marca
        self.qtdMinimoEstoque = qtdMinimoEstoque
        self.qtdEstoque = qtdEstoque
        self.qtdAlterarEstoque = qtdAlterarEstoque
        self.valorUnitario = valorUnitario
        self.totalEstoque = totalEstoque
        self.query = query

    # Recendo ultimo ID inserido
    def lastIdProduto(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            ultimo = sessao.query(Produto.id).order_by(desc(Produto.id)).limit(1).first()
            self.id = ultimo.id + 1
            sessao.close()
        except:
            self.id = 1
        return self.id

    # Cadastro de Produto
    def addProduto(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            row = Produto(
                id = self.id,
                produto = self.produto,
                descricao = self.descricao,
                imagem = self.imagem,
                categoria = self.categoria,
                marca = self.marca,
                qtdMinimoEstoque = self.qtdMinimoEstoque,
                qtdEstoque = self.qtdEstoque,
                valorUnitario = self.valorUnitario
            )
            # Add query na sessao
            sessao.add(row)
            # Executando a Query
            sessao.commit()
            sessao.close()
        except IntegrityError:
            self.updateProduto()

    # Update de Produto
    def updateProduto(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Selecionando id
            query = sessao.query(Produto).get(self.id)
            # Novos Valores
            query.id = self.id
            query.produto = self.produto
            query.descricao = self.descricao
            query.imagem = self.imagem
            query.categoria = self.categoria
            query.marca = self.marca
            query.qtdMinimoEstoque = self.qtdMinimoEstoque
            query.qtdEstoque = self.qtdEstoque
            query.valorUnitario = self.valorUnitario
            # Executando a Query
            sessao.commit()
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Busca por ID
    def DetalhamentoProdutoId(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            busca = sessao.query(Produto).get(self.id)
            # Salvando resultado da Query
            self.id = busca.id
            self.produto = busca.produto
            self.descricao = busca.descricao
            self.imagem = busca.imagem
            self.categoria = busca.categoria
            self.marca = busca.marca
            self.qtdMinimoEstoque = busca.qtdMinimoEstoque
            self.qtdEstoque = busca.qtdEstoque
            self.valorUnitario = busca.valorUnitario
            sessao.close()
        except:
            pass

    # Busca Produto por Nome
    def listaProduto(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = (sessao.query(Produto.id, Produto.produto, Produto.descricao,
                                       Produto.imagem, Produto.categoria, Produto.marca,
                                       Produto.qtdMinimoEstoque, Produto.qtdEstoque, Produto.valorUnitario,
                                       CategoriaProduto.categoria_produto,
                                       MarcaProduto.marca_produto
                                       )
                          .join(CategoriaProduto)
                          .join(MarcaProduto)
                          .filter(Produto.produto.contains(self.produto))
                          .order_by(Produto.id)
                          )
            self.query.all()
            self.id = []
            self.produto = []
            self.descricao = []
            self.imagem = []
            self.categoria = []
            self.marca = []
            self.qtdMinimoEstoque = []
            self.qtdEstoque = []
            self.valorUnitario = []
            self.totalEstoque = []
            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.produto.append(row.produto)
                self.descricao.append(row.descricao)
                self.imagem.append(row.imagem)
                self.categoria.append(row.categoria_produto)
                self.marca.append(row.marca_produto)
                self.qtdMinimoEstoque.append(row.qtdMinimoEstoque)
                self.qtdEstoque.append(row.qtdEstoque)
                self.valorUnitario.append(row.valorUnitario)
                self.totalEstoque.append(float(row.valorUnitario) * int(row.qtdEstoque))
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Busca produto por Nome Autocomplete
    def buscaProdutoNome(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            self.query = sessao.query(Produto.id, Produto.produto).filter(
                Produto.produto == self.produto).first()
            # Salvando resultado
            self.id = self.query.id
            sessao.close()
            pass
        except:
            self.produto = 'Produto Não Encontrado'

    # Entrada Produto no estoque
    def entradaEstoque(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Selecionando ID Produto
            row = sessao.query(Produto).get(self.id)
            row.qtdEstoque = float(row.qtdEstoque) + float(self.qtdAlterarEstoque)
            sessao.commit()
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Lista produtos com estoque abaixo do minimo
    def listaEstoqueBaixo(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            row = sessao.query(Produto).filter(Produto.qtdEstoque < Produto.qtdMinimoEstoque).count()
            sessao.close()
        except IntegrityError as err:
            print(err)
        return row

    # Lista total de Produtos
    def totalProdutoCadastrado(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            row = sessao.query(Produto).count()
            sessao.close()
        except IntegrityError as err:
            print(err)
        return row
