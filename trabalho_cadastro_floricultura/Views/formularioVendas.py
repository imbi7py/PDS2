# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formVendas.ui',
# licensing of 'formVendas.ui' applies.
#
# Created: Mon Feb 11 12:25:23 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormVendas(object):
    def setFormVendas(self, ct_FormVenda):
        ct_FormVenda.setObjectName("ct_FormVenda")
        ct_FormVenda.resize(1000, 500)
        ct_FormVenda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormVenda.setFrameShadow(QtWidgets.QFrame.Raised)

        self.fr_FormVendas = QtWidgets.QFrame(ct_FormVenda)
        self.fr_FormVendas.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormVendas.setStyleSheet("background: #FFF;\nborder: none")
        self.fr_FormVendas.setObjectName("fr_FormVendas")

        styleTbItens = "QTableView{\n" \
        "color: #28292A;\n" \
        "font-weight: bold;\n" \
        "font-size: 11px;\n" \
        "background: #FFF;\n" \
        "padding: 0 0 0 5px;\n" \
        "}\n" \
        "QHeaderView:section{\n" \
        "background: #FFF;\n" \
        "padding: 5px 0 ;\n" \
        "font-size: 11px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #797979;\n" \
        "border: none;\n" \
        "border-bottom: 2px solid #CCC;\n" \
        "text-transform: uppercase;\n" \
        "margin: 0 2px 0 0;\n" \
        "}\n" \
        "QTableView::item {\n" \
        "border-bottom: 2px solid #CCC;\n" \
        "padding: 2px;\n" \
        "margin: 0 2px 0 0;\n" \
        "}"

        styleLbTitulo = "QLabel{\n" \
        "font-size: 14px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #A2A2A2;\n" \
        "}"

        styleIdVenda = "QLineEdit{\n" \
        "background: #7AB32E;\n" \
        "border-radius: 2px;\n" \
        "color: #000;\n" \
        "font: 16px \"Arial\" ;\n" \
        "font-weight: bold;\n" \
        "color: #FFF\n" \
        "}\n"

        styleLbItem = "QLabel{\n" \
        "font-size: 9px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #FFF;\n" \
        "border: none;\n" \
        "}"

        styleLbFinanceiro = "QLabel{\n" \
        "font-size: 10px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #40a286;\n" \
        "border: none\n" \
        "}"

        styleLbFinanceiroEscuro = "QLabel{\n" \
        "font-size: 13px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #7B7A7A;\n" \
        "border: none\n" \
        "}"

        styleLbAzul = "QLabel{\n" \
        "font-size: 12px;\n" \
        "font-family: \"Arial Unicode MS\";\n" \
        "color: #7AB32E;\n" \
        "border: none;\n" \
        "}"

        styleTxCampos = "QLineEdit{\n" \
        "background: #CFCFCF;\n" \
        "border-radius: 2px;\n" \
        "color: #000;\n" \
        "font: 13px \"Arial\";\n" \
        "text-transform: uppercase;\n" \
        "}\n" \
        "QLineEdit:Focus {\n" \
        "border: 1px solid red;\n" \
        "}"

        styleTxFinanceiro = "font-size: 24px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #7AB32E;\n" \
        "border: none\n"

        styleTxItens = "QLineEdit{\n" \
        "background: #40a286;\n" \
        "border-radius: 2px;\n" \
        "color: #000;\n" \
        "font: 10px \"Arial\" ;\n" \
        "font-weight: bold;\n" \
        "color: #FFF;\n" \
        "text-transform: uppercase\n" \
        "}"

        styleCbCampos = "QComboBox{\n" \
        "background: #CFCFCF;\n" \
        "border-radius: 2px;\n" \
        "color: #000;\n" \
        "font: 13px \"Arial\" ;\n" \
        "text-transform: uppercase\n" \
        "}\n" \
        "QComboBox:Focus {\n" \
        "border: 1px solid red;\n" \
        "}\n" \
        " QComboBox::drop-down {\n" \
        "     subcontrol-origin: padding;\n" \
        "     subcontrol-position: top right;\n" \
        "     width: 25px;\n" \
        "     border-left-width: 1px;\n" \
        "     border-left-color: darkgray;\n" \
        "     border-left-style: solid; /* just a single line */\n" \
        "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n" \
        "     border-bottom-right-radius: 3px;\n" \
        "}\n" \
        "QComboBox::down-arrow {\n" \
        "     image: url(Images/down.png);\n" \
        "}\n"

        styleBotaoSalvar = "QPushButton {\n" \
        "background-color: #7AB32E;\n" \
        "color: #FFF\n" \
        "}\n" \
        "QPushButton:hover{\n" \
        "background-color: #40a286\n" \
        "}"

        styleBotaoVoltar = "QPushButton {\n" \
        "background-color: #1E87F0;\n" \
        "color: #FFF\n" \
        "}\n" \
        "QPushButton:hover{\n" \
        "background-color: #40a286\n" \
        "}"

        styleBotaoIncluir = "QPushButton {\n" \
        "background: rgb(57, 151, 54);\n" \
        "color: #FFF\n" \
        "}\n" \
        "QPushButton:hover{\n" \
        "background-color: #7AB32E\n" \
        "}"

        fontTahoma = QtGui.QFont()
        fontTahoma.setFamily("Tahoma")
        fontTahoma.setPointSize(10)
        fontTahoma.setWeight(75)
        fontTahoma.setBold(True)

        fontArial = QtGui.QFont()
        fontArial.setFamily("Arial")
        fontArial.setPointSize(16)
        fontArial.setWeight(75)
        fontArial.setBold(True)

        """ Dados Cadastrais Cliente """

        self.lb_TituloFormProduto = QtWidgets.QLabel(self.fr_FormVendas)
        self.lb_TituloFormProduto.setGeometry(QtCore.QRect(20, 10, 960, 20))
        self.lb_TituloFormProduto.setStyleSheet(styleLbTitulo)
        self.lb_TituloFormProduto.setObjectName("lb_TituloFormProduto")

        self.fr_topoPedido = QtWidgets.QFrame(self.fr_FormVendas)
        self.fr_topoPedido.setGeometry(QtCore.QRect(20, 30, 960, 40))
        self.fr_topoPedido.setStyleSheet("QFrame{\nbackground: #FFF;\nborder: 1px solid #7AB32E;\n}\n")
        self.fr_topoPedido.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_topoPedido.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_topoPedido.setObjectName("fr_topoPedido")

        self.tx_IdVenda = QtWidgets.QLineEdit(self.fr_topoPedido)
        self.tx_IdVenda.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.tx_IdVenda.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IdVenda.setStyleSheet(styleIdVenda)
        self.tx_IdVenda.setText("")
        self.tx_IdVenda.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_IdVenda.setReadOnly(True)
        self.tx_IdVenda.setPlaceholderText("")
        self.tx_IdVenda.setObjectName("tx_IdVenda")

        self.lb_IdCliente = QtWidgets.QLabel(self.fr_topoPedido)
        self.lb_IdCliente.setGeometry(QtCore.QRect(120, 2, 100, 18))
        self.lb_IdCliente.setStyleSheet(styleLbAzul)
        self.lb_IdCliente.setObjectName("lb_IdCliente")

        self.tx_IdCliente = QtWidgets.QLineEdit(self.fr_topoPedido)
        self.tx_IdCliente.setGeometry(QtCore.QRect(120, 18, 100, 18))
        self.tx_IdCliente.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IdCliente.setStyleSheet(styleTxCampos)
        self.tx_IdCliente.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_IdCliente.setObjectName("tx_IdCliente")

        self.lb_NomeCliente = QtWidgets.QLabel(self.fr_topoPedido)
        self.lb_NomeCliente.setGeometry(QtCore.QRect(240, 2, 100, 18))
        self.lb_NomeCliente.setStyleSheet(styleLbAzul)
        self.lb_NomeCliente.setObjectName("lb_NomeCliente")

        self.tx_NomeCliente = QtWidgets.QLineEdit(self.fr_topoPedido)
        self.tx_NomeCliente.setGeometry(QtCore.QRect(240, 18, 350, 18))
        self.tx_NomeCliente.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NomeCliente.setStyleSheet(styleTxCampos)
        self.tx_NomeCliente.setReadOnly(True)
        self.tx_NomeCliente.setObjectName("tx_NomeCliente")

        """ Dados Cadastrais Itens """

        self.lb_ItensTitulo = QtWidgets.QLabel(self.fr_FormVendas)
        self.lb_ItensTitulo.setGeometry(QtCore.QRect(20, 80, 120, 20))
        self.lb_ItensTitulo.setStyleSheet(styleLbTitulo)
        self.lb_ItensTitulo.setObjectName("lb_ItensTitulo")

        self.fr_addProduto = QtWidgets.QFrame(self.fr_FormVendas)
        self.fr_addProduto.setGeometry(QtCore.QRect(20, 100, 600, 40))
        self.fr_addProduto.setStyleSheet("QFrame{\nbackground: #40a286;\nborder: 1px solid #1E87F0;\n}\n")
        self.fr_addProduto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_addProduto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fr_addProduto.setObjectName("fr_addProduto")

        self.tx_IdBuscaItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_IdBuscaItem.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.tx_IdBuscaItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_IdBuscaItem.setStyleSheet(styleTxItens)
        self.tx_IdBuscaItem.setText("")
        self.tx_IdBuscaItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_IdBuscaItem.setReadOnly(False)
        self.tx_IdBuscaItem.setObjectName("tx_IdBuscaItem")

        self.tx_NomeProdutoItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_NomeProdutoItem.setGeometry(QtCore.QRect(40, 0, 270, 40))
        self.tx_NomeProdutoItem.setMouseTracking(True)
        self.tx_NomeProdutoItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NomeProdutoItem.setStyleSheet(styleTxItens)
        self.tx_NomeProdutoItem.setText("")
        self.tx_NomeProdutoItem.setFrame(False)
        self.tx_NomeProdutoItem.setCursorPosition(0)
        self.tx_NomeProdutoItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_NomeProdutoItem.setReadOnly(True)
        self.tx_NomeProdutoItem.setObjectName("tx_NomeProdutoItem")

        self.tx_QtdItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_QtdItem.setGeometry(QtCore.QRect(310, 0, 40, 40))
        self.tx_QtdItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_QtdItem.setStyleSheet(styleTxItens)
        self.tx_QtdItem.setText("")
        self.tx_QtdItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_QtdItem.setReadOnly(False)
        self.tx_QtdItem.setObjectName("tx_QtdItem")

        self.lb_ValorUnitarioItem = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_ValorUnitarioItem.setGeometry(QtCore.QRect(350, 0, 75, 15))
        self.lb_ValorUnitarioItem.setStyleSheet(styleLbItem)
        self.lb_ValorUnitarioItem.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_ValorUnitarioItem.setObjectName("lb_ValorUnitarioItem")

        self.tx_ValorUnitarioItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ValorUnitarioItem.setGeometry(QtCore.QRect(350, 15, 75, 25))
        self.tx_ValorUnitarioItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorUnitarioItem.setStyleSheet(styleTxItens)
        self.tx_ValorUnitarioItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ValorUnitarioItem.setReadOnly(True)
        self.tx_ValorUnitarioItem.setObjectName("tx_ValorUnitarioItem")

        self.lb_ValorTotalItem = QtWidgets.QLabel(self.fr_addProduto)
        self.lb_ValorTotalItem.setGeometry(QtCore.QRect(425, 0, 75, 15))
        self.lb_ValorTotalItem.setStyleSheet(styleLbItem)
        self.lb_ValorTotalItem.setObjectName("lb_ValorTotalItem")

        self.tx_ValorTotalItem = QtWidgets.QLineEdit(self.fr_addProduto)
        self.tx_ValorTotalItem.setGeometry(QtCore.QRect(425, 15, 75, 25))
        self.tx_ValorTotalItem.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorTotalItem.setStyleSheet(styleTxItens)
        self.tx_ValorTotalItem.setText("")
        self.tx_ValorTotalItem.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_ValorTotalItem.setReadOnly(True)
        self.tx_ValorTotalItem.setObjectName("tx_ValorTotalItem")

        self.bt_IncluirItem = QtWidgets.QPushButton(self.fr_addProduto)
        self.bt_IncluirItem.setEnabled(False)
        self.bt_IncluirItem.setGeometry(QtCore.QRect(500, 0, 100, 40))
        self.bt_IncluirItem.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_IncluirItem.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_IncluirItem.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_IncluirItem.setStyleSheet(styleBotaoIncluir)
        self.bt_IncluirItem.setText("")
        self.bt_IncluirItem.setIconSize(QtCore.QSize(75, 35))
        self.bt_IncluirItem.setObjectName("bt_IncluirItem")

        self.tb_Itens = QtWidgets.QTableWidget(self.fr_FormVendas)
        self.tb_Itens.setGeometry(QtCore.QRect(20, 150, 600, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_Itens.sizePolicy().hasHeightForWidth())
        self.tb_Itens.setSizePolicy(sizePolicy)
        self.tb_Itens.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tb_Itens.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Itens.setStyleSheet(styleTbItens)
        self.tb_Itens.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Itens.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Itens.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Itens.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tb_Itens.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tb_Itens.setAutoScrollMargin(20)
        self.tb_Itens.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Itens.setTabKeyNavigation(False)
        self.tb_Itens.setProperty("showDropIndicator", False)
        self.tb_Itens.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Itens.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Itens.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tb_Itens.setShowGrid(False)
        self.tb_Itens.setCornerButtonEnabled(False)
        self.tb_Itens.setRowCount(0)
        self.tb_Itens.setObjectName("tb_Itens")
        self.tb_Itens.setColumnCount(7)
        self.tb_Itens.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Itens.setHorizontalHeaderItem(6, item)

        self.tb_Itens.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Itens.horizontalHeader().setStretchLastSection(True)
        self.tb_Itens.verticalHeader().setVisible(False)
        self.tb_Itens.verticalHeader().setCascadingSectionResizes(True)
        self.tb_Itens.verticalHeader().setDefaultSectionSize(40)

        """ Dados Cadastrais Financeiro Final """

        self.fr_financeiroPedido = QtWidgets.QFrame(self.fr_FormVendas)
        self.fr_financeiroPedido.setGeometry(QtCore.QRect(640, 100, 340, 130))
        self.fr_financeiroPedido.setStyleSheet("background: #F1F1F1;\n" \
                                                "border-top: 4px solid #40a286;\n" \
                                                "border-bottom: 4px solid #40a286;")
        self.fr_financeiroPedido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_financeiroPedido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_financeiroPedido.setObjectName("fr_financeiroPedido")

        self.lb_SubTotal = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_SubTotal.setGeometry(QtCore.QRect(0, 5, 100, 20))
        self.lb_SubTotal.setStyleSheet(styleLbFinanceiro)
        self.lb_SubTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_SubTotal.setObjectName("lb_SubTotal")

        self.tx_SubTotal = QtWidgets.QLineEdit(self.fr_financeiroPedido)
        self.tx_SubTotal.setGeometry(QtCore.QRect(0, 25, 100, 25))
        self.tx_SubTotal.setStyleSheet(styleTxFinanceiro)
        self.tx_SubTotal.setText("")
        self.tx_SubTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_SubTotal.setReadOnly(True)
        self.tx_SubTotal.setObjectName("tx_SubTotal")

        self.lb_Desconto = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_Desconto.setGeometry(QtCore.QRect(120, 5, 90, 20))
        self.lb_Desconto.setStyleSheet(styleLbFinanceiroEscuro)
        self.lb_Desconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_Desconto.setObjectName("lb_Desconto")

        self.tx_Desconto = QtWidgets.QLineEdit(self.fr_financeiroPedido)
        self.tx_Desconto.setGeometry(QtCore.QRect(120, 25, 90, 25))
        self.tx_Desconto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Desconto.setStyleSheet(styleTxFinanceiro)
        self.tx_Desconto.setInputMask("")
        self.tx_Desconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_Desconto.setObjectName("tx_Desconto")

        self.lb_TotalFinal = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_TotalFinal.setGeometry(QtCore.QRect(220, 5, 100, 20))
        self.lb_TotalFinal.setStyleSheet(styleLbFinanceiro)
        self.lb_TotalFinal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_TotalFinal.setObjectName("lb_TotalFinal")

        self.tx_TotalFinal = QtWidgets.QLineEdit(self.fr_financeiroPedido)
        self.tx_TotalFinal.setEnabled(False)
        self.tx_TotalFinal.setGeometry(QtCore.QRect(220, 25, 100, 25))
        self.tx_TotalFinal.setStyleSheet(styleTxFinanceiro)
        self.tx_TotalFinal.setText("")
        self.tx_TotalFinal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_TotalFinal.setReadOnly(True)
        self.tx_TotalFinal.setObjectName("tx_TotalFinal")

        self.lb_TipoPagamento = QtWidgets.QLabel(self.fr_financeiroPedido)
        self.lb_TipoPagamento.setGeometry(QtCore.QRect(20, 60, 250, 15))
        self.lb_TipoPagamento.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_TipoPagamento.setStyleSheet(styleLbFinanceiro)
        self.lb_TipoPagamento.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_TipoPagamento.setObjectName("lb_TipoPagamento")

        self.cb_TipoPagamento = QtWidgets.QComboBox(self.fr_financeiroPedido)
        self.cb_TipoPagamento.setGeometry(QtCore.QRect(20, 80, 300, 25))
        self.cb_TipoPagamento.setStyleSheet(styleCbCampos)
        self.cb_TipoPagamento.setObjectName("cb_FormaPagamento")

        """ Frame Actions """

        self.fr_BotoesFormVendas = QtWidgets.QFrame(self.fr_FormVendas)
        self.fr_BotoesFormVendas.setGeometry(QtCore.QRect(0, 460, 1000, 40))
        self.fr_BotoesFormVendas.setStyleSheet("background:#E1DFE0;\nborder: none;")
        self.fr_BotoesFormVendas.setObjectName("fr_BotoesFormVendas")

        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormVendas)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 0, 120, 30))
        self.bt_Voltar.setFont(fontTahoma)
        self.bt_Voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Voltar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Voltar.setStyleSheet(styleBotaoVoltar)
        self.bt_Voltar.setObjectName("bt_Voltar")

        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormVendas)
        self.bt_Salvar.setGeometry(QtCore.QRect(750, 0, 120, 30))
        self.bt_Salvar.setFont(fontTahoma)
        self.bt_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet(styleBotaoSalvar)
        self.bt_Salvar.setObjectName("bt_Salvar")


        """ End """

        self.translateUiFormVendas(ct_FormVenda)
        QtCore.QMetaObject.connectSlotsByName(ct_FormVenda)
        ct_FormVenda.setTabOrder(self.tx_IdVenda, self.tx_IdCliente)
        ct_FormVenda.setTabOrder(self.tx_IdCliente, self.tx_NomeCliente)
        ct_FormVenda.setTabOrder(self.tx_NomeCliente, self.tx_IdBuscaItem)
        ct_FormVenda.setTabOrder(self.tx_IdBuscaItem, self.tx_NomeProdutoItem)
        ct_FormVenda.setTabOrder(self.tx_NomeProdutoItem, self.tx_QtdItem)
        ct_FormVenda.setTabOrder(self.tx_QtdItem, self.tx_ValorUnitarioItem)
        ct_FormVenda.setTabOrder(self.tx_ValorUnitarioItem, self.tx_ValorTotalItem)
        ct_FormVenda.setTabOrder(self.tx_ValorTotalItem, self.tx_SubTotal)
        ct_FormVenda.setTabOrder(self.tx_SubTotal, self.tx_Desconto)
        ct_FormVenda.setTabOrder(self.tx_Desconto, self.tx_TotalFinal)
        ct_FormVenda.setTabOrder(self.tx_TotalFinal, self.cb_TipoPagamento)
        ct_FormVenda.setTabOrder(self.cb_TipoPagamento, self.tb_Itens)

    def translateUiFormVendas(self, ct_FormVenda):
        _translate = QtCore.QCoreApplication.translate
        ct_FormVenda.setWindowTitle(_translate("ct_FormVenda", "Frame", None, -1))
        self.lb_TituloFormProduto.setText(_translate("ct_FormVenda", "VENDA", None, -1))
        """ Dados Cadastrais Cliente """
        self.lb_IdCliente.setText(_translate("ct_FormVenda", "CÓD. CLIENTE", None, -1))
        self.tx_IdCliente.setPlaceholderText(_translate("ct_FormVenda", "0", None, -1))
        self.lb_NomeCliente.setText(_translate("ct_FormVenda", "CLIENTE", None, -1))
        self.tx_NomeCliente.setPlaceholderText(_translate("ct_FormVenda", "NOME CLIENTE", None, -1))
        """ Dados Cadastrais Produtos Venda """
        self.lb_ItensTitulo.setText(_translate("ct_FormVenda", "ITENS", None, -1))
        self.tx_IdBuscaItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "CÓD", None, -1))
        self.tx_NomeProdutoItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "DIGITE O NOME  DO ITEM", None, -1))
        self.tx_QtdItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "QTD.", None, -1))
        self.lb_ValorUnitarioItem.setText(QtWidgets.QApplication.translate("ct_FormVenda", "UNITÁRIO (R$)", None, -1))
        self.tx_ValorUnitarioItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "0.00", None, -1))
        self.lb_ValorTotalItem.setText(QtWidgets.QApplication.translate("ct_FormVenda", "TOTAL (R$)", None, -1))
        self.tx_ValorTotalItem.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "0.00", None, -1))
        """ Tabela Itens selecionados """
        self.tb_Itens.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ct_FormVenda", "ID (PRODUTO)", None, -1))
        self.tb_Itens.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ct_FormVenda", "PRODUTO", None, -1))
        self.tb_Itens.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("ct_FormVenda", "QUANTIDADE", None, -1))
        self.tb_Itens.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("ct_FormVenda", "UNITÁRIO (R$)", None, -1))
        self.tb_Itens.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("ct_FormVenda", "TOTAL (R$)", None, -1))
        self.tb_Itens.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("ct_FormVenda", "EXCLUIR", None, -1))
        """ Tabela Dados Pagamento Venda """
        self.lb_SubTotal.setText(QtWidgets.QApplication.translate("ct_FormVenda", "SUBTOTAL (R$)", None, -1))
        self.tx_SubTotal.setText(QtWidgets.QApplication.translate("ct_FormVenda", "0.00", None, -1))
        self.lb_Desconto.setText(QtWidgets.QApplication.translate("ct_FormVenda", "DESCONTO", None, -1))
        self.tx_Desconto.setText(QtWidgets.QApplication.translate("ct_FormVenda", "0.00", None, -1))
        self.tx_Desconto.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "0.00", None, -1))
        self.lb_TotalFinal.setText(QtWidgets.QApplication.translate("ct_FormVenda", "TOTAL FINAL (R$)", None, -1))
        self.tx_TotalFinal.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormVenda", "0.00", None, -1))
        self.lb_TipoPagamento.setText(QtWidgets.QApplication.translate("ct_FormVenda", "FORMA DE PAGAMENTO", None, -1))
        self.cb_TipoPagamento.setItemText(0, _translate("ct_FormVenda", "SELECIONE"))
        """ Ações """
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormVenda", "VOLTAR", None, -1))
        self.bt_Salvar.setText(QtWidgets.QApplication.translate("ct_FormVenda", "SALVAR", None, -1))
        self.bt_IncluirItem.setText(QtWidgets.QApplication.translate("ct_FormVenda", "INCLUIR ITEM", None, -1))
