# -*- coding: utf-8 -*-

#
# mainclientes is responsable for managing the Customer information in the GUI
#

import re
from functools import partial

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from Views.janelaClientes import Ui_ct_MainClientes
from Views.formularioCliente import Ui_ct_FormClientes
from Crud.CrudCliente import CrudCliente
from Crud.CrudVenda import CrudVenda

class MainClientes(Ui_ct_MainClientes, Ui_ct_FormClientes):

    """funcao junta GUI e dados para janela de Clientes"""
    def mainclientes(self, frame):
        super(MainClientes, self).setMainClientes(frame)
        self.frameMainClientes.show()

        # Icone Botao busca Janela
        self.IconeBotaoMenu(self.bt_BuscaClientes, self.resourcepath('Images/iconSearch.png'))

        # Campo Busca
        self.tx_BuscaClientes.textEdited.connect(self.ListarCliente)
        # Botao Adicionar Cliente
        self.bt_AddNovoClientes.clicked.connect(self.FormClientes)

        # Desabilitando Signals tabela
        self.tb_Clientes.blockSignals(True)
        # define tamanho colunas tabela
        self.tb_Clientes.setColumnHidden(0, True)
        self.tb_Clientes.setColumnWidth(1, 50)
        self.tb_Clientes.setColumnWidth(2, 200)
        self.tb_Clientes.setColumnWidth(3, 200)
        self.tb_Clientes.setColumnWidth(4, 200)
        self.tb_Clientes.setColumnWidth(5, 200)
        self.tb_Clientes.setColumnWidth(6, 50)
        # Populando Tabela
        self.ListarCliente()

    """Lista Dados Tabela"""
    def ListarCliente(self):
        lista = CrudCliente()
        # se o texto ta vazio vai buscar tudo
        lista.nome = self.tx_BuscaClientes.text()
        lista.listaCliente()

        while self.tb_Clientes.rowCount() > 0:
            self.tb_Clientes.removeRow(0)

        i = 0
        # lista.nome vira array apos select
        if len(lista.nome) >= 1:
            while i < len(lista.nome):
                self.tb_Clientes.insertRow(i)
                self.alinharDadosTabela(self.tb_Clientes, i, 0, str(lista.id[i]))
                self.SetTabelaID(self.tb_Clientes, i, 1, lista.id[i])
                self.SetFormataDadosPessoaisTabela(self.tb_Clientes, i, 2,
                                        lista.nome[i],
                                        lista.sobrenome[i])
                self.SetFormataDadosPessoaisTabela(self.tb_Clientes, i, 3,
                                        "CPF: " + lista.cpf[i],
                                        "RG: " + lista.rg[i])
                self.SetFormataDadosPessoaisTabela(self.tb_Clientes, i, 4,
                                        self.formatoNumTelefone(lista.celular[i]),
                                        self.formatoNumTelefone(lista.telefone[i]))
                self.SetFormataDadosPessoaisTabela(self.tb_Clientes, i, 5, lista.email[i], "")
                # click edit
                self.botaoTabela(self.tb_Clientes, i, 6,
                                partial(self.DetalhamentoCliente, lista.id[i]), "#7AB32E")
                i += 1

    """Drilldown Cliente por ID"""
    def DetalhamentoCliente(self, valor):
        id = valor
        self.FormClientes()
        self.tx_Id.setText(str(id))

        busca = CrudCliente()
        busca.id = self.tx_Id.text()
        busca.DetalhamentoClienteId()

        # if hasattr(busca, 'imagem') and busca.imagem:
        #     pixmap = QPixmap()
        #     pixmap.loadFromData(QByteArray.fromBase64(busca.imagem))
        #     self.lb_FotoCliente.setPixmap(pixmap.scaledToWidth(150, Qt.TransformationMode(Qt.FastTransformation)))
        #     self.bt_AdicionarImagem.setHidden(True)
        #     self.bt_DeletarImagem.setVisible(True)
        self.tx_NomeCliente.setText(busca.nome)
        self.tx_Sobrenome.setText(busca.sobrenome)
        self.tx_CPF.setText(busca.cpf)
        self.tx_RG.setText(busca.rg)
        self.tx_Celular.setText(busca.celular)
        self.tx_Telefone.setText(busca.telefone)
        self.tx_Email.setText(busca.email)
        self.tx_Observacao.setText(busca.obs)
        self.tx_CEP.setText(busca.cep)
        self.tx_Endereco.setText(busca.endereco)
        self.tx_Numero.setText(busca.numero)
        self.tx_Bairro.setText(busca.bairro)
        self.tx_Cidade.setText(busca.cidade)
        self.tx_Estado.setText(busca.estado)

    """Frame Formulário Cliente"""
    def FormClientes(self):
        self.DesativaBotaoClientes()
        self.LimpaFrame(self.ct_containerClientes)
        super(MainClientes, self).setFormClientes(self.ct_containerClientes)
        self.fr_FormClientes.show()
        # Checando se existe ID válido
        self.IdCheckCliente()
        # Icone Botoes
        self.bt_BuscaCep.clicked.connect(self.buscarCepCliente)

        # Buscar Cep
        self.tx_CEP.returnPressed.connect(self.buscarCepCliente)
        self.IconeBotaoMenu(self.bt_BuscaCep, self.resourcepath('Images/find.png'))

        # acoes
        self.bt_Voltar.clicked.connect(self.janelaClientes)
        self.bt_Salvar.clicked.connect(self.ValidarDadosCliente)

    # checando campo Id se é Edicao ou Novo Cliente
    def IdCheckCliente(self):
        if not self.tx_Id.text():
            busca = CrudCliente()
            self.tx_Id.setText(str(busca.lastIdCliente()))

    # Valida campos necessarios
    def ValidarDadosCliente(self):
        if not self.tx_NomeCliente.text():
            self.tx_NomeCliente.setFocus()
        elif not self.tx_Sobrenome.text():
            self.tx_Sobrenome.setFocus()
        elif not self.tx_CPF.text():
            self.tx_CPF.setFocus()
        elif not self.tx_RG.text():
            self.tx_RG.setFocus()
        elif not self.tx_RG.text():
            self.tx_Celular.setFocus()
        elif not self.tx_Email.text():
            self.tx_Email.setFocus()
        else:
            self.CadastraClienteDB()

    def CadastraClienteDB(self):
        INSERIR = CrudCliente()
        INSERIR.id = self.tx_Id.text()
        INSERIR.nome = self.tx_NomeCliente.text().upper()
        INSERIR.sobrenome = self.tx_Sobrenome.text().upper()
        INSERIR.cpf = re.sub('[^[0-9]', '', self.tx_CPF.text())
        INSERIR.rg = re.sub('[^[0-9]', '', self.tx_RG.text())
        INSERIR.celular = re.sub('[^[0-9]', '', self.tx_Celular.text())
        INSERIR.telefone = re.sub('[^[0-9]', '', self.tx_Telefone.text())
        INSERIR.email = self.tx_Email.text()
        INSERIR.obs = self.tx_Observacao.text().upper()

        INSERIR.cep = re.sub('[^[0-9]', '', self.tx_CEP.text())
        INSERIR.endereco = self.tx_Endereco.text().upper()
        INSERIR.numero = self.tx_Numero.text()
        INSERIR.bairro = self.tx_Bairro.text().upper()
        INSERIR.cidade = self.tx_Cidade.text().upper()
        INSERIR.estado = self.tx_Estado.text().upper()
        INSERIR.addCliente()
        self.janelaClientes()

    def DesativaBotaoClientes(self):
        self.bt_AddNovoClientes.setEnabled(False)
        self.tx_BuscaClientes.setEnabled(False)
        self.tx_BuscaClientes.setEnabled(False)

    def AtivaBotaoClientes(self):
        self.bt_AddNovoClientes.setEnabled(True)
        self.tx_BuscaClientes.setEnabled(True)
        self.bt_BuscaClientes.setEnabled(True)

    # def UploadImagem(self):
    #     Dialog = QFileDialog()
    #     Dialog.setOption(QFileDialog.DontUseNativeDialog, True)
    #     filename = Dialog.getOpenFileName(self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

    #     self.lb_FotoCliente.setPixmap(QPixmap(filename).scaledToWidth(
    #         150, Qt.TransformationMode(Qt.FastTransformation)))
    #     self.bt_AdicionarImagem.setHidden(True)
    #     self.bt_DeletarImagem.setVisible(True)

    # def DeleteImagem(self):
    #     self.lb_FotoCliente.clear()
    #     self.bt_DeletarImagem.setHidden(True)
    #     self.bt_AdicionarImagem.setVisible(True)
