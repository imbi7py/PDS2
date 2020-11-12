# -*- coding: utf-8 -*-

#
# janelaProdutos is responsable for managing GUI elements of Product tab
#
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_MainProdutos(object):
    def setMainProdutos(self, ct_MainProdutos):
        ct_MainProdutos.setObjectName("ct_MainProdutos")
        ct_MainProdutos.resize(1000, 600)
        ct_MainProdutos.setStyleSheet("border:none")

        self.frameMainProdutos = QtWidgets.QFrame(ct_MainProdutos)
        self.frameMainProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainProdutos.setObjectName("frameMainProdutos")

        fontArial = QtGui.QFont()
        fontArial.setFamily("Arial")

        fontDejavu = QtGui.QFont()
        fontDejavu.setFamily("DejaVu Sans")
        fontDejavu.setPointSize(18)
        fontDejavu.setBold(True)
        fontDejavu.setWeight(75)

        styleOptionButton = "QPushButton {\n" \
        "background-color: #7AB32E;\n" \
        "color: #FFF;\n" \
        "}\n" \
        "QPushButton:hover{\n" \
        "background-color: #40a286\n" \
        "}"

        styleTxtEscuro = "QLineEdit {\n" \
        "color: #000\n" \
        "}\n"

        styleTabela = "QTableView{\n" \
        "color: #797979;\n" \
        "font-weight: bold;\n" \
        "font-size: 13px;\n" \
        "background: #FFF;\n" \
        "padding: 0 0 0 5px;\n" \
        "}\n" \
        "QHeaderView:section{\n" \
        "background: #FFF;\n" \
        "padding: 5px 0 ;\n" \
        "font-size: 12px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #797979;\n" \
        "border: none;\n" \
        "border-bottom: 2px solid #CCC;\n" \
        "text-transform: uppercase\n" \
        "}\n" \
        "QTableView::item {\n" \
        "border-bottom: 2px solid #CCC;\n" \
        "padding: 2px;\n" \
        "}\n"

        """ Header Pagina de Clientes """

        self.fr_TituloProdutos = QtWidgets.QFrame(self.frameMainProdutos)
        self.fr_TituloProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloProdutos.setStyleSheet("border: none")
        self.fr_TituloProdutos.setObjectName("fr_TituloProdutos")
        
        self.lb_tituloProdutos = QtWidgets.QLabel(self.fr_TituloProdutos)
        self.lb_tituloProdutos.setGeometry(QtCore.QRect(10, 15, 200, 30))
        self.lb_tituloProdutos.setFont(fontDejavu)
        self.lb_tituloProdutos.setStyleSheet("color: #959595")
        self.lb_tituloProdutos.setObjectName("lb_tituloProdutos")

        """ Frame de Busca e Adicionar """

        self.fr_TopoMenuProdutos = QtWidgets.QFrame(self.frameMainProdutos)
        self.fr_TopoMenuProdutos.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuProdutos.setStyleSheet("background:#E1DFE0;\n"
                                               "border: none;")
        self.fr_TopoMenuProdutos.setObjectName("fr_TopoMenuProdutos")

        self.tx_BuscaProdutos = QtWidgets.QLineEdit(self.fr_TopoMenuProdutos)
        self.tx_BuscaProdutos.setGeometry(QtCore.QRect(5, 5, 800, 30))
        self.tx_BuscaProdutos.setFont(fontArial)
        self.tx_BuscaProdutos.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaProdutos.setStyleSheet(styleTxtEscuro)
        self.tx_BuscaProdutos.setObjectName("tx_BuscaProdutos")

        self.bt_BuscaProdutos = QtWidgets.QPushButton(self.fr_TopoMenuProdutos)
        self.bt_BuscaProdutos.setGeometry(QtCore.QRect(820, 5, 30, 30))
        self.bt_BuscaProdutos.setFont(fontArial)
        self.bt_BuscaProdutos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_BuscaProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaProdutos.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaProdutos.setText("")
        self.bt_BuscaProdutos.setObjectName("bt_BuscaProdutos")

        self.bt_AddNovoProdutos = QtWidgets.QPushButton(self.fr_TopoMenuProdutos)
        self.bt_AddNovoProdutos.setGeometry(QtCore.QRect(857, 0, 140, 40))
        self.bt_AddNovoProdutos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_AddNovoProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoProdutos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoProdutos.setStyleSheet(styleOptionButton)
        self.bt_AddNovoProdutos.setText("")
        self.bt_AddNovoProdutos.setObjectName("bt_AddNovoProdutos")

        """ Frame Tabela """

        self.ct_containerProdutos = QtWidgets.QFrame(self.frameMainProdutos)
        self.ct_containerProdutos.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerProdutos.setStyleSheet("border: none")
        self.ct_containerProdutos.setObjectName("ct_containerProdutos")

        self.tb_Produtos = QtWidgets.QTableWidget(self.ct_containerProdutos)
        self.tb_Produtos.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        #self.tb_Produtos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Produtos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Produtos.setStyleSheet(styleTabela)
        self.tb_Produtos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Produtos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Produtos.setAutoScrollMargin(20)
        self.tb_Produtos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Produtos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Produtos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Produtos.setShowGrid(False)
        self.tb_Produtos.setGridStyle(QtCore.Qt.NoPen)
        self.tb_Produtos.setWordWrap(False)
        self.tb_Produtos.setRowCount(0)
        self.tb_Produtos.setObjectName("tb_Produtos")
        self.tb_Produtos.setColumnCount(8)

        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)

        item = QtWidgets.QTableWidgetItem()
        self.tb_Produtos.setHorizontalHeaderItem(0, item)
        item = self.createItem(True)
        item.setBackground(QtGui.QColor(0, 0, 0, 0))
        item.setForeground(brush)
        self.tb_Produtos.setHorizontalHeaderItem(1, item)
        item = self.createItem()
        item.setForeground(brush)
        self.tb_Produtos.setHorizontalHeaderItem(2, item)
        item = self.createItem()
        item.setForeground(brush)
        self.tb_Produtos.setHorizontalHeaderItem(3, item)
        item = self.createItem(True)
        item.setForeground(brush)
        self.tb_Produtos.setHorizontalHeaderItem(4, item)
        item = self.createItem(True)
        item.setForeground(brush)
        self.tb_Produtos.setHorizontalHeaderItem(5, item)
        item = self.createItem(True)
        item.setForeground(brush)
        self.tb_Produtos.setHorizontalHeaderItem(6, item)
        item = self.createItem(True)
        self.tb_Produtos.setHorizontalHeaderItem(7, item)

        self.tb_Produtos.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Produtos.horizontalHeader().setHighlightSections(False)
        self.tb_Produtos.horizontalHeader().setStretchLastSection(True)
        self.tb_Produtos.verticalHeader().setVisible(False)
        self.tb_Produtos.verticalHeader().setDefaultSectionSize(40)
        self.tb_Produtos.verticalHeader().setMinimumSectionSize(20)

        self.ct_containerProdutos.raise_()
        self.fr_TopoMenuProdutos.raise_()
        self.fr_TituloProdutos.raise_()

        self.translateUiProdutos(ct_MainProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_MainProdutos)

    def createItem(self, alignAll=False):
        fontSegoe = QtGui.QFont()
        fontSegoe.setFamily("Segoe UI")
        fontSegoe.setPointSize(10)
        fontSegoe.setBold(True)
        fontSegoe.setWeight(75)

        item = QtWidgets.QTableWidgetItem()
        if alignAll == True:
            item.setTextAlignment(QtCore.Qt.AlignHCenter |
                              QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        else:
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        item.setFont(fontSegoe)
        return item

    def translateUiProdutos(self, ct_MainProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_MainProdutos.setWindowTitle(_translate("ct_MainProdutos", "Frame"))
        self.tx_BuscaProdutos.setPlaceholderText(
            _translate("ct_MainProdutos", "PROCURAR POR..."))
        item = self.tb_Produtos.horizontalHeaderItem(1)
        item.setText(_translate("ct_MainProdutos", "ID"))
        item = self.tb_Produtos.horizontalHeaderItem(2)
        item.setText(_translate("ct_MainProdutos", "NOME"))
        item = self.tb_Produtos.horizontalHeaderItem(3)
        item.setText(_translate("ct_MainProdutos", "CATEGORIA"))
        item = self.tb_Produtos.horizontalHeaderItem(4)
        item.setText(_translate("ct_MainProdutos", "ESTOQUE"))
        item = self.tb_Produtos.horizontalHeaderItem(5)
        item.setText(_translate("ct_MainProdutos", "VALOR UNITÁRIO"))
        item = self.tb_Produtos.horizontalHeaderItem(6)
        item.setText(_translate("ct_MainProdutos", "TOTAL"))
        item = self.tb_Produtos.horizontalHeaderItem(7)
        item.setText(_translate("ct_MainProdutos", "EDITAR"))
        self.lb_tituloProdutos.setText(
            _translate("ct_MainProdutos", "PRODUTOS"))
        self.bt_AddNovoProdutos.setText(
            _translate("ct_MainProdutos", "NOVO PRODUTO"))