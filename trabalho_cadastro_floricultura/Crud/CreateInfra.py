# coding=utf-8
import sys
import os
import configparser

from sqlalchemy.exc import ProgrammingError

from Crud.ConectorDB import Conexao, Base
from Crud.Models import *

class CreateDb(object):
    def __init__(self, dbhandler="", DbHost="127.0.0.1", DbName="floricultura", DbUser="root",
                 DbPassword="zpesystems", conecta="", erro=""):
        self.DbHost = DbHost
        self.DbName = DbName
        self.DbUser = DbUser
        self.DbPassword = DbPassword
        self.conecta = conecta
        self.erro = erro
        self.dbhandler = dbhandler

        # Caminho absoluto config.ini
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        config = configparser.ConfigParser()
        config.sections()

    def createDB(self):
        # Caso banco não exista, Cria
        import mysql.connector
        try:
            conn = mysql.connector.connect(
                user=self.DbUser, password=self.DbPassword, host=self.DbHost)
            cursor = conn.cursor()
            cursor.execute('SET sql_notes = 0 ;')
            # cursor.execute('drop database %s;' % self.DbName)
            cursor.execute("create database IF NOT EXISTS %s" %
                           self.DbName)

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                self.erro = 1  # Erro User e Senha
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.erro = 2  # erro banco de dados inexistente
            else:
                self.erro == err

    def tabelas(self):
        return
        conecta = Conexao()
        try:
            Base.metadata.create_all(conecta.engine)
            # Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            sessao.add_all([
                FormaPagamento(id=1, forma_pagamento='Dinheiro'),
                FormaPagamento(id=2, forma_pagamento='Cartão'),
                CategoriaProduto(id=1, categoria_produto='Plantas'),
                CategoriaProduto(id=2, categoria_produto='Vasos e Cachepôs'),
                CategoriaProduto(id=3, categoria_produto='Insumos'),
                CategoriaProduto(id=4, categoria_produto='Ferramentas'),
                CategoriaProduto(id=5, categoria_produto='Moveis'),
                CategoriaProduto(id=6, categoria_produto='Decoracao'),
                CategoriaProduto(id=7, categoria_produto='Flores de Corte'),
                MarcaProduto(id=1, marca_produto='Arbustos'),
                MarcaProduto(id=2, marca_produto='Árvores de Sombra'),
                MarcaProduto(id=3, marca_produto='Árvores Frutíferas'),
                MarcaProduto(id=4, marca_produto='Cactáceas e Suculentas'),
                MarcaProduto(id=5, marca_produto='Ervas'),
                MarcaProduto(id=6, marca_produto='Cachepôs'),
                MarcaProduto(id=7, marca_produto='Enfeites'),
                MarcaProduto(id=8, marca_produto='Presentes'),
                MarcaProduto(id=9, marca_produto='Vasos'),
                MarcaProduto(id=10, marca_produto='Adubos e Fertilizantes'),
                MarcaProduto(id=11, marca_produto='Defensivos'),
                MarcaProduto(id=12, marca_produto='Pedras e Terra'),
                MarcaProduto(id=13, marca_produto='Irrigação'),
                MarcaProduto(id=14, marca_produto='Pergolados'),
                MarcaProduto(id=15, marca_produto='Arranjos'),
                MarcaProduto(id=16, marca_produto='Flores Avulsas'),
                MarcaProduto(id=17, marca_produto='Buquês'),
                Cliente(id=0, nome="ANONIMO", sobrenome="ANONIMO", cpf="00000000000", rg="0000000", email="ANONIMO@ANONIMO.COM")
            ])
            sessao.commit()
        except Exception as e:
            print("ERRO: "+e)
            pass
