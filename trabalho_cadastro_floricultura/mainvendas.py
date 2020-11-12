# -*- coding: utf-8 -*-

#
# mainvendas is responsable for managing the Product information in the GUI
#

from functools import partial
from datetime import datetime, timezone 

from PyQt5.QtCore import Qt, QByteArray, QUrl, QBuffer
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

from Views.janelaVendas import Ui_ct_MainVendas
from Views.formularioVendas import Ui_ct_FormVendas

from Crud.CrudCliente import CrudCliente
from Crud.CrudProduto import CrudProduto
from Crud.CrudVenda import CrudVenda
from Crud.CrudRelVenda import CrudRelVenda
from Crud.CrudFormaPagamento import CrudFormaPagamento

class MainVendas(Ui_ct_MainVendas, Ui_ct_FormVendas):
    # funcao junta GUI e dados para janela de Vendas
    def mainvendas(self, frame):
        super(MainVendas, self).setMainVendas(frame)
        self.frameMainVendas.show()

        # Icone Botao busca Janela
        self.IconeBotaoMenu(self.bt_BuscaVendas,
                            self.resourcepath('Images/iconSearch.png'))
        # Campo Busca
        self.tx_BuscaVendas.textEdited.connect(self.ListarVenda)
        # Botao Adicionar Venda
        self.bt_AddNovoVendas.clicked.connect(self.FormVendas)

        # Desabilitando Signals tabela
        self.tb_Vendas.blockSignals(True)
        # define tamanho colunas tabela
        self.tb_Vendas.setColumnHidden(0, True)
        self.tb_Vendas.setColumnWidth(1, 50)
        self.tb_Vendas.setColumnWidth(2, 250)
        self.tb_Vendas.setColumnWidth(3, 200)
        self.tb_Vendas.setColumnWidth(4, 200)
        self.tb_Vendas.setColumnWidth(5, 150)
        self.tb_Vendas.setColumnWidth(6, 50)

        # Populando tabela vendas
        self.ListarVenda()

    # Dados Tabela Venda
    def ListarVenda(self):
        lista = CrudVenda()
        # se o texto ta vazio vai buscar tudo
        lista.venda = self.tx_BuscaVendas.text()
        lista.listaVenda()

        while self.tb_Vendas.rowCount() > 0:
            self.tb_Vendas.removeRow(0)

        i = 0
        # lista.venda vira array apos select
        if len(lista.id) >= 1:
            while i < len(lista.id):
                self.tb_Vendas.insertRow(i)
                self.alinharDadosTabela(self.tb_Vendas, i, 0, str(lista.id[i]))
                self.SetTabelaID(self.tb_Vendas, i, 1, lista.id[i])
                self.SetFormataDadosPessoaisTabela(self.tb_Vendas, i, 2,
                                        "%s %s" % (lista.nomeCliente[i], lista.sobrenomeCliente[i]),
                                        "ID: " + str(lista.idCliente[i]))
                self.SetFormataDadosPessoaisTabela(self.tb_Vendas, i, 3, lista.tipoPagamento[i], "")
                self.SetFormataDadosPessoaisTabela(self.tb_Vendas, i, 4, lista.dataVenda[i], "")
                self.SetValorTable(self.tb_Vendas, i, 5, lista.valorTotal[i])
                # click edit
                self.botaoTabela(self.tb_Vendas, i, 6, partial(self.DetalhamentoVenda, lista.id[i]), "#7AB32E")
                i += 1

    """Drilldown Venda por ID"""
    def DetalhamentoVenda(self, valor):
        id = valor
        self.FormVendas()
        self.tx_IdVenda.setText(str(id))

        busca = CrudVenda()
        busca.id = id
        busca.DetalhamentoVendaId()
        self.tx_IdCliente.setText(str(busca.idCliente))
        self.cb_TipoPagamento.setCurrentIndex(self.cb_TipoPagamento.findData(busca.tipoPagamento))
        data = busca.dataVenda
        # add todos os itens na tabela
        lista = CrudRelVenda()
        lista.idVenda = id
        lista.listaItens()

        while self.tb_Itens.rowCount() > 0:
            self.tb_Itens.removeRow(0)

        i = 0
        if len(lista.id) >= 1:
            while i < len(lista.id):
                self.tx_IdBuscaItem.setText(str(lista.id[i]))
                self.tx_NomeProdutoItem.setText(str(lista.produto[i]))
                self.tx_QtdItem.setText(str(lista.qtd[i]))
                self.tx_ValorUnitarioItem.setText(str(lista.valorUnitario[i]))
                self.tx_ValorTotalItem.setText(str(lista.valorTotal[i]))
                self.AddItemTabela(False)
                i += 1

        self.BuscaClienteId()
        self.tx_Desconto.setText(str(busca.desconto))
        self.TotalFinal()

        # disable add item...
        for filho in self.fr_addProduto.findChildren(QLineEdit):
            filho.clear()
            filho.setDisabled(True)
        self.bt_IncluirItem.setDisabled(True)
        self.tx_Desconto.setDisabled(True)
        self.cb_TipoPagamento.setDisabled(True)
        self.tx_IdCliente.setDisabled(True)

    """Frame Formulário Venda"""
    def FormVendas(self):
        self.DesativaBotaoVendas()
        self.LimpaFrame(self.ct_containerVendas)
        super(MainVendas, self).setFormVendas(self.ct_containerVendas)
        self.fr_FormVendas.show()

        # Checando se existe ID válido
        self.IdCheckVenda()
        # Icone Botoes
        self.IconeBotaoMenu(self.bt_BuscaVendas, self.resourcepath('Images/iconSearch.png'))

        # Validar campos int
        validarInt = QIntValidator(0, 999, self)
        # Validar campos float
        validarValorFloat = QDoubleValidator(0.50, 999.99, 2, self)
        validarValorFloat.setNotation(QDoubleValidator.StandardNotation)
        validarValorFloat.setDecimals(2)

        self.tx_QtdItem.setValidator(validarInt)
        self.tx_ValorUnitarioItem.setValidator(validarValorFloat)
        self.tx_ValorTotalItem.setValidator(validarValorFloat)
        self.tx_SubTotal.setValidator(validarValorFloat)
        self.tx_Desconto.setValidator(validarValorFloat)
        self.tx_TotalFinal.setValidator(validarValorFloat)

        # Botao Add Categoria e populando combobox e check
        self.ListaTipoPagamento()
        # busca cliente e produto
        self.tx_IdCliente.returnPressed.connect(self.BuscaClienteId)
        self.tx_IdCliente.textEdited.connect(self.BuscaClienteId)
        self.tx_IdBuscaItem.returnPressed.connect(self.BuscaProdutoId)
        self.tx_IdBuscaItem.textEdited.connect(self.BuscaProdutoId)
        # calculo total item
        self.tx_QtdItem.returnPressed.connect(self.TotalItem)
        self.tx_QtdItem.textEdited.connect(self.TotalItem)
        # Calculo valor final da venda
        self.tx_Desconto.returnPressed.connect(self.TotalFinal)
        self.tx_Desconto.textEdited.connect(self.TotalFinal)
        # Add item no carrinho de compra
        self.bt_IncluirItem.clicked.connect(self.ValidaDadosAddItem)
        # acoes
        self.bt_Voltar.clicked.connect(self.janelaVendas)
        self.bt_Salvar.clicked.connect(self.ValidarDadosVenda)

        self.tb_Itens.blockSignals(True)
        self.tb_Itens.setColumnHidden(0, True)
        self.tb_Itens.resizeRowsToContents()
        self.tb_Itens.setColumnWidth(1, 100)
        self.tb_Itens.setColumnWidth(2, 100)
        self.tb_Itens.setColumnWidth(3, 100)
        self.tb_Itens.setColumnWidth(4, 100)
        self.tb_Itens.setColumnWidth(5, 100)
        self.tb_Itens.setColumnWidth(6, 100)

    # checando campo Id se é Edicao ou Novo Venda
    def IdCheckVenda(self):
        if not self.tx_IdVenda.text():
            busca = CrudVenda()
            self.tx_IdVenda.setText(str(busca.lastIdVenda()))

    # Verificando Dados para finalizar a venda
    def ValidarDadosVenda(self):
        if not self.tx_IdVenda.text():
            self.tx_IdVenda.setFocus()
            return
        elif not self.tx_IdCliente.text():
            msg = QMessageBox()
            msg.setWindowTitle("Alerta de Identificacao")
            msg.setText("Cliente não foi identificado.")
            msg.setInformativeText("Você deseja prosseguir com cliente anonimo?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.Yes);

            returnValue = msg.exec()
            if returnValue == QMessageBox.Yes:
                self.tx_IdCliente.setText("1")
            elif returnValue == QMessageBox.No:
                self.tx_IdCliente.setFocus()
                return
            else:
                print("Erro: Opção inexistente: %d", returnValue)
                return

        elif not self.tx_SubTotal.text() or self.tx_SubTotal.text() == "0.00":
            self.tx_SubTotal.setFocus()
            return
        elif not self.tx_TotalFinal.text() or self.tx_TotalFinal.text() == "0.00":
            self.tx_TotalFinal.setFocus()
            return

        ESTOQUE = CrudProduto()
        ITEMS = {}
        QTDESTOQUE = {}
        for row in range(self.tb_Itens.rowCount()):
            idProduto = self.tb_Itens.item(row, 1).text()
            qtd = self.tb_Itens.item(row, 3).text()
            if idProduto in ITEMS:
                ITEMS[idProduto] = ITEMS.get(idProduto, 0) - int(qtd)
            else:
                ESTOQUE.id = idProduto
                ESTOQUE.DetalhamentoProdutoId()
                ITEMS[idProduto] = ESTOQUE.qtdEstoque - int(qtd)
                QTDESTOQUE[idProduto] = ESTOQUE.qtdEstoque

        campos = ""
        for element in ITEMS:
            if ITEMS.get(element, 0) < 0:
                campos = campos + "\nID %s: %s unidades," % (str(element), str(QTDESTOQUE.get(element, 0)))

        if campos != "":
            campos = campos[0:-1]
            msg = QMessageBox()
            msg.setWindowTitle("Alerta de Estoque")
            msg.setText("Produtos na venda excedem a quantidade em Estoque.")
            msg.setInformativeText("ID: Quantidade de estoque, abaixo:%s" % campos)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok);
            returnValue = msg.exec()
            return
        self.CadastraVendaDB()

    # Cadastro Venda
    def CadastraVendaDB(self):
        # current datetime in UTC
        dt = datetime.now() 
        utc_time = dt.replace(tzinfo=timezone.utc) 

        INSERIR = CrudVenda()
        INSERIR.id = self.tx_IdVenda.text()
        INSERIR.idCliente = self.tx_IdCliente.text().upper()
        INSERIR.tipoPagamento = self.cb_TipoPagamento.currentData()
        INSERIR.dataVenda = utc_time
        INSERIR.subtotal = self.tx_SubTotal.text().replace(",", ".")
        INSERIR.desconto = self.tx_Desconto.text().replace(",", ".")
        INSERIR.addVenda()

        ATUALIZAR_ESTOQUE = CrudProduto()
        INSERIR_ITENS = CrudRelVenda()
        for row in range(self.tb_Itens.rowCount()):
            idProduto = self.tb_Itens.item(row, 1).text()
            qtd = self.tb_Itens.item(row, 3).text()
            INSERIR_ITENS.idVenda = self.tx_IdVenda.text()
            INSERIR_ITENS.idProduto = idProduto
            INSERIR_ITENS.qtd = qtd
            INSERIR_ITENS.valorUnitario = self.tb_Itens.item(row, 4).text()
            INSERIR_ITENS.valorTotal = self.tb_Itens.item(row, 5).text()
            INSERIR_ITENS.addItens()
            ATUALIZAR_ESTOQUE.id = idProduto
            ATUALIZAR_ESTOQUE.DetalhamentoProdutoId()
            ATUALIZAR_ESTOQUE.qtdEstoque = int(ATUALIZAR_ESTOQUE.qtdEstoque) - int(qtd)
            ATUALIZAR_ESTOQUE.updateProduto()
        self.janelaVendas()

    def DesativaBotaoVendas(self):
        self.bt_AddNovoVendas.setEnabled(False)
        self.tx_BuscaVendas.setEnabled(False)
        self.bt_BuscaVendas.setEnabled(False)

    def AtivaBotaoVendas(self):
        self.bt_AddNovoVendas.setEnabled(True)
        self.tx_BuscaVendas.setEnabled(True)
        self.bt_BuscaVendas.setEnabled(True)

    # Populando combobox forma de pagamento
    def ListaTipoPagamento(self, busca=True):
        busca = CrudFormaPagamento()
        busca.listaFormaPagamento()
        self.cb_TipoPagamento.clear()
        i = 0
        if busca == True:
            self.cb_TipoPagamento.addItem("Ambos", 0)
            i = 1
        for lista in busca.formaPagamento:
            self.cb_TipoPagamento.addItem(lista, str(busca.id[i]))
            i += 1

    # Valida dados para add itens para uma venda.
    def ValidaDadosAddItem(self):
        if not self.tx_IdVenda.text():
            self.tx_IdVenda.setFocus()
        elif not self.tx_IdBuscaItem.text():
            self.tx_IdBuscaItem.setFocus()
        elif not self.tx_NomeProdutoItem.text():
            self.tx_NomeProdutoItem.setFocus()
        elif not self.tx_QtdItem.text():
            self.tx_QtdItem.setFocus()
        elif not self.tx_ValorUnitarioItem.text():
            self.tx_ValorUnitarioItem.setFocus()
        elif not self.tx_ValorTotalItem.text():
            self.tx_ValorTotalItem.setFocus()
        else:
            self.AddItemTabela()

    # Adiciona Item a tabela
    def AddItemTabela(self, withRemove=True):
        row = self.tb_Itens.rowCount()
        self.tb_Itens.insertRow(row)
        self.alinharDadosTabela(self.tb_Itens, row, 0, self.tx_IdBuscaItem.text())
        self.alinharDadosTabela(self.tb_Itens, row, 1, self.tx_IdBuscaItem.text())
        self.alinharDadosTabelaEsquerda(self.tb_Itens, row, 2, self.tx_NomeProdutoItem.text())
        self.alinharDadosTabela(self.tb_Itens, row, 3, self.tx_QtdItem.text().replace(',', '.'))
        self.alinharDadosTabela(self.tb_Itens, row, 4, self.tx_ValorUnitarioItem.text())
        self.alinharDadosTabela(self.tb_Itens, row, 5, self.tx_ValorTotalItem.text())
        if withRemove == True:
            self.botaoRemoveItem(self.tb_Itens, row, 6, partial(self.RemoveLinha, row), "#40a286")
        self.TotalFinal()
        self.LimpaCampoAddProduto()

    # Limpando campos após adicionar produdo
    def LimpaCampoAddProduto(self):
        for filho in self.fr_addProduto.findChildren(QLineEdit):
            filho.clear()
        self.bt_IncluirItem.setDisabled(True)
        self.tx_IdBuscaItem.setFocus()

    # Calcular total de item
    def TotalItem(self):
        totalItem = 0
        if self.tx_QtdItem.text() and self.tx_ValorUnitarioItem.text():
            valorUnitario = self.tx_ValorUnitarioItem.text().replace(',', '.')
            totalItem = int(self.tx_QtdItem.text()) * float(valorUnitario)
        self.tx_ValorTotalItem.setText(format(totalItem, ".2f"))
        self.bt_IncluirItem.setDisabled(False)

    # Removendo item da tabela
    def RemoveLinha(self, linha):
        self.tb_Itens.removeRow(linha)
        # precisa prq as linhas sao movidas
        for row in range(self.tb_Itens.rowCount()):
            self.botaoRemoveItem(self.tb_Itens, row, 6, partial(self.RemoveLinha, row), "#40a286")
        self.TotalFinal()

    # Calcular total de Venda
    def TotalFinal(self):
        total = 0
        if int(self.tb_Itens.rowCount()) == 0:
            self.tx_SubTotal.setText(format(total, ".2f"))
            self.tx_Desconto.setText(format(total, ".2f"))
            self.tx_TotalFinal.setText(format(total, ".2f"))
            return
        for row in range(self.tb_Itens.rowCount()):
            if self.tb_Itens.item(row, 5).text():
                total = float(self.tb_Itens.item(row, 5).text()) + total
            else:
                total = -1
                print("Erro: valor total invalido")
        self.tx_SubTotal.setText(format(total, ".2f"))
        self.tx_TotalFinal.setText(format(total, ".2f"))

        if self.tx_Desconto.text():
            desconto = self.tx_Desconto.text().replace(',', '.')
            TotalFinal = float(total) - float(desconto)
            self.tx_TotalFinal.setText(format(TotalFinal, ".2f"))
            self.tx_Desconto.setText(format(float(desconto), ".2f"))

    # atualizar valor total estoque
    def AtualizarTotalEstoque(self):
        if not self.tx_QtdEstoque.text():
            return
        if not self.tx_ValorUnitario.text():
            return
        total = int(self.tx_QtdEstoque.text()) * float(self.tx_ValorUnitario.text())
        self.tx_TotalEstoque.setText(str(total))

    # Busca produtos por ID
    def BuscaProdutoId(self):
        if not self.tx_IdBuscaItem.text():
            self.LimpaCampoAddProduto()
            return  
        id = int(self.tx_IdBuscaItem.text())
        busca = CrudProduto()
        busca.id = id
        busca.DetalhamentoProdutoId()
        if busca.produto:
            self.tx_NomeProdutoItem.setText(busca.produto)
            self.tx_ValorUnitarioItem.setText(str(busca.valorUnitario))
            self.tx_QtdItem.setFocus()
        else:
            self.LimpaCampoAddProduto()
            self.tx_NomeProdutoItem.setText("Produto não encontrado")
            self.tx_IdBuscaItem.setFocus()

    # Busca cliente por ID
    def BuscaClienteId(self):
        if not self.tx_IdCliente.text():
            self.tx_NomeCliente.clear()
            return            
        id = int(self.tx_IdCliente.text())
        busca = CrudCliente()
        busca.id = id
        busca.DetalhamentoClienteId()
        if busca.nome:
            self.tx_NomeCliente.setText("%s %s" % (busca.nome, busca.sobrenome))
            self.tx_NomeCliente.setFocus()
        else:
            self.tx_NomeCliente.setText("Cliente não encontrado")
            self.tx_IdCliente.clear()
            self.tx_IdCliente.setFocus()
