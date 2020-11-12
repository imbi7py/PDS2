# -*- coding: utf-8 -*-

#
# janelaVendas is responsable for managing GUI elements of Sell tab
#
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_MainVendas(object):
    def setMainVendas(self, ct_MainVendas):
        ct_MainVendas.setObjectName("ct_MainVendas")
        ct_MainVendas.resize(1000, 600)
        ct_MainVendas.setStyleSheet("border:none")

        self.frameMainVendas = QtWidgets.QFrame(ct_MainVendas)
        self.frameMainVendas.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frameMainVendas.setObjectName("frameMainVendas")

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

        styleLbDate = "QLabel{\n" \
        "font-size: 12px;\n" \
        "font-family: \"Arial Unicode MS\";\n" \
        "\n" \
        "color: #7AB32E;\n" \
        "border: none;\n" \
        "}"

        styleCbPagamento = "QComboBox{\n" \
        "background: #E1DFE0;\n" \
        "border: none;\n" \
        "font-family: \"Arial\";\n" \
        "font-size: 11px;\n" \
        "font-weight: bold;\n" \
        "color: rgb(80,79,79)\n" \
        "}\n" \
        "QComboBox::drop-down {\n" \
        "     subcontrol-origin: padding;\n" \
        "     subcontrol-position: top right;\n" \
        "     width: 18px;\n" \
        "     border-left-width: 1px;\n" \
        "     border-left-color: darkgray;\n" \
        "     border-left-style: solid; /* just a single line */\n" \
        "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n" \
        "     border-bottom-right-radius: 3px;\n" \
        " }\n" \
        "QComboBox::down-arrow {\n" \
        "     image: url(Images/down.png);\n" \
        "}\n"

        """ Header Pagina """

        self.fr_TituloVendas = QtWidgets.QFrame(self.frameMainVendas)
        self.fr_TituloVendas.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.fr_TituloVendas.setStyleSheet("border: none")
        self.fr_TituloVendas.setObjectName("fr_TituloVendas")
        
        self.lb_tituloVendas = QtWidgets.QLabel(self.fr_TituloVendas)
        self.lb_tituloVendas.setGeometry(QtCore.QRect(10, 15, 200, 30))
        self.lb_tituloVendas.setFont(fontDejavu)
        self.lb_tituloVendas.setStyleSheet("color: #959595")
        self.lb_tituloVendas.setObjectName("lb_tituloVendas")

        """ Frame de Busca e Adicionar """

        self.fr_TopoMenuVendas = QtWidgets.QFrame(self.frameMainVendas)
        self.fr_TopoMenuVendas.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.fr_TopoMenuVendas.setStyleSheet("background:#E1DFE0;\nborder: none;")
        self.fr_TopoMenuVendas.setObjectName("fr_TopoMenuVendas")

        self.tx_BuscaVendas = QtWidgets.QLineEdit(self.fr_TopoMenuVendas)
        self.tx_BuscaVendas.setGeometry(QtCore.QRect(5, 5, 780, 30))
        self.tx_BuscaVendas.setFont(fontArial)
        self.tx_BuscaVendas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_BuscaVendas.setStyleSheet(styleTxtEscuro)
        self.tx_BuscaVendas.setObjectName("tx_BuscaVendas")

        self.bt_BuscaVendas = QtWidgets.QPushButton(self.fr_TopoMenuVendas)
        self.bt_BuscaVendas.setGeometry(QtCore.QRect(820, 5, 30, 30))
        self.bt_BuscaVendas.setFont(fontArial)
        self.bt_BuscaVendas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_BuscaVendas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_BuscaVendas.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_BuscaVendas.setText("")
        self.bt_BuscaVendas.setObjectName("bt_BuscaVendas")

        self.bt_AddNovoVendas = QtWidgets.QPushButton(self.fr_TopoMenuVendas)
        self.bt_AddNovoVendas.setGeometry(QtCore.QRect(857, 0, 140, 40))
        self.bt_AddNovoVendas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_AddNovoVendas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_AddNovoVendas.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_AddNovoVendas.setStyleSheet(styleOptionButton)
        self.bt_AddNovoVendas.setText("")
        self.bt_AddNovoVendas.setObjectName("bt_AddNovoVendas")

        """ Frame Tabela """

        self.ct_containerVendas = QtWidgets.QFrame(self.frameMainVendas)
        self.ct_containerVendas.setGeometry(QtCore.QRect(0, 100, 1000, 500))
        self.ct_containerVendas.setStyleSheet("border: none")
        self.ct_containerVendas.setObjectName("ct_containerVendas")

        self.tb_Vendas = QtWidgets.QTableWidget(self.ct_containerVendas)
        self.tb_Vendas.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        #self.tb_Vendas.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Vendas.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_Vendas.setStyleSheet(styleTabela)
        self.tb_Vendas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_Vendas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_Vendas.setAutoScrollMargin(20)
        self.tb_Vendas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_Vendas.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_Vendas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_Vendas.setShowGrid(False)
        self.tb_Vendas.setGridStyle(QtCore.Qt.NoPen)
        self.tb_Vendas.setWordWrap(False)
        self.tb_Vendas.setRowCount(0)
        self.tb_Vendas.setObjectName("tb_Vendas")
        self.tb_Vendas.setColumnCount(7)

        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)

        item = QtWidgets.QTableWidgetItem()
        self.tb_Vendas.setHorizontalHeaderItem(0, item)
        item = self.createItem(True)
        item.setBackground(QtGui.QColor(0, 0, 0, 0))
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(1, item)
        item = self.createItem()
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(2, item)
        item = self.createItem()
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(3, item)
        item = self.createItem()
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(4, item)
        item = self.createItem(True)
        item.setForeground(brush)
        self.tb_Vendas.setHorizontalHeaderItem(5, item)
        item = self.createItem(True)
        self.tb_Vendas.setHorizontalHeaderItem(6, item)

        self.tb_Vendas.horizontalHeader().setDefaultSectionSize(120)
        self.tb_Vendas.horizontalHeader().setHighlightSections(False)
        self.tb_Vendas.horizontalHeader().setStretchLastSection(True)
        self.tb_Vendas.verticalHeader().setVisible(False)
        self.tb_Vendas.verticalHeader().setDefaultSectionSize(40)
        self.tb_Vendas.verticalHeader().setMinimumSectionSize(20)

        self.ct_containerVendas.raise_()
        self.fr_TopoMenuVendas.raise_()
        self.fr_TituloVendas.raise_()

        self.translateUiVendas(ct_MainVendas)
        QtCore.QMetaObject.connectSlotsByName(ct_MainVendas)

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

    def translateUiVendas(self, ct_MainVendas):
        _translate = QtCore.QCoreApplication.translate
        ct_MainVendas.setWindowTitle(_translate("ct_MainVendas", "Frame"))
        self.tx_BuscaVendas.setPlaceholderText(_translate("ct_MainVendas", "PROCURAR POR..."))
        item = self.tb_Vendas.horizontalHeaderItem(1)
        item.setText(_translate("ct_MainVendas", "ID"))
        item = self.tb_Vendas.horizontalHeaderItem(2)
        item.setText(_translate("ct_MainVendas", "CLIENTE"))
        item = self.tb_Vendas.horizontalHeaderItem(3)
        item.setText(_translate("ct_MainVendas", "PAGAMENTO"))
        item = self.tb_Vendas.horizontalHeaderItem(4)
        item.setText(_translate("ct_MainVendas", "DATA E HORA"))
        item = self.tb_Vendas.horizontalHeaderItem(5)
        item.setText(_translate("ct_MainVendas", "VALOR TOTAL"))
        item = self.tb_Vendas.horizontalHeaderItem(6)
        item.setText(_translate("ct_MainVendas", "VER"))
        self.lb_tituloVendas.setText(
            _translate("ct_MainVendas", "VENDAS"))
        self.bt_AddNovoVendas.setText(
            _translate("ct_MainVendas", "NOVA VENDA"))