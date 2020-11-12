# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from Crud.ConectorDB import Conexao
from Crud.Models import Cliente

class CrudCliente(object):
    def __init__(self, id="", nome="", sobrenome="", cpf="", rg="",
                 celular="", telefone="", email="", obs="", cep="",
                 endereco="", numero="", bairro="", cidade="", estado="",
                 dataVenda="", Total="", idPedido="", query=""):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.rg = rg
        self.celular = celular
        self.telefone = telefone
        self.email = email
        self.obs = obs
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.query = query

    # Recebendo última id inserido
    def lastIdCliente(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            ultimo = sessao.query(Cliente).order_by(
                desc(Cliente.id)).limit(1).first()
            self.id = ultimo.id + 1
            sessao.close()
            pass
        except:
            self.id = 1
        return self.id

    #  Cadastro Cliente
    def addCliente(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            row = Cliente(
                id=self.id,
                nome=self.nome,
                sobrenome=self.sobrenome,
                cpf=self.cpf,
                rg=self.rg,
                celular=self.celular,
                telefone=self.telefone,
                email=self.email,
                obs=self.obs,
                cep=self.cep,
                endereco=self.endereco,
                numero=self.numero,
                bairro=self.bairro,
                cidade=self.cidade,
                estado=self.estado
            )
            # Execurando a Query
            sessao.add(row)
            sessao.commit()
            sessao.close()
        except IntegrityError:
            self.updateCliente()

    #  Update Cliente
    def updateCliente(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Selecionando id
            query = sessao.query(Cliente).get(self.id)
            # Novos valores
            query.nome = self.nome
            query.sobrenome = self.sobrenome
            query.cpf = self.cpf
            query.rg = self.rg
            query.celular = self.celular
            query.telefone = self.telefone
            query.email = self.email
            query.obs = self.obs
            query.cep = self.cep
            query.endereco = self.endereco
            query.numero = self.numero
            query.bairro = self.bairro
            query.cidade = self.cidade
            query.estado = self.estado
            # Execurando a Query
            sessao.commit()
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Buscando cliente por ID
    def DetalhamentoClienteId(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            busca = sessao.query(Cliente).get(self.id)
            # Salvando resultado da Query
            self.id = busca.id
            self.nome = busca.nome
            self.sobrenome = busca.sobrenome
            self.cpf = busca.cpf
            self.rg = busca.rg
            self.celular = busca.celular
            self.telefone = busca.telefone
            self.email = busca.email
            self.obs = busca.obs
            self.cep = busca.cep
            self.endereco = busca.endereco
            self.numero = busca.numero
            self.bairro = busca.bairro
            self.cidade = busca.cidade
            self.estado = busca.estado
            sessao.close()
        except:
            pass

    # Buscando Cliente por nome
    def listaCliente(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = (sessao.query(Cliente)
                    .filter(Cliente.nome.contains(self.nome))
                    .order_by(Cliente.id)
                    )
            self.query.all()
            # Convertendo variaveis em lista
            self.id = []
            self.nome = []
            self.sobrenome = []
            self.cpf = []
            self.rg = []
            self.celular = []
            self.telefone = []
            self.email = []
            # Salvando resultado da query e suas listas
            for row in self.query:
                self.id.append(row.id)
                self.nome.append(row.nome)
                self.sobrenome.append(row.sobrenome)
                self.cpf.append(row.cpf)
                self.rg.append(row.rg)
                self.celular.append(row.celular)
                self.telefone.append(row.telefone)
                self.email.append(row.email)
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)

    # Lista AutoComplete Cliente
    def autoCompleteCliente(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = sessao.query(Cliente).filter(
                Cliente.nome.contains(self.nome))
            self.query.all()
            # Convertendo variavel em lista
            self.nome = []
            # salvando resultado em lista
            for row in self.query:
                self.nome.append(row.nome)
            sessao.close()
            pass
        except IntegrityError as err:
            print("ERRO: " + err)

    # Busca CLiente por nome
    def buscaClienteNome(self):
        try:
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            self.query = sessao.query(Cliente).filter(
                Cliente.nome == self.nome).first()
            # Salvando Resultado
            self.id = self.query.id
            self.nome = self.query.nome
            self.celular = self.query.celular
            sessao.close()
        except IntegrityError as err:
            print("ERRO: " + err)
