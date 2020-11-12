# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormProdutos(object):
    def setFormProdutos(self, ct_FormProdutos):
        ct_FormProdutos.setObjectName("ct_FormProdutos")
        ct_FormProdutos.resize(1000, 500)
        ct_FormProdutos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormProdutos.setFrameShadow(QtWidgets.QFrame.Raised)

        self.fr_FormProdutos = QtWidgets.QFrame(ct_FormProdutos)
        self.fr_FormProdutos.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormProdutos.setStyleSheet("background: #FFF;\nborder: none")
        self.fr_FormProdutos.setObjectName("fr_FormProdutos")

        styleHTabela = "QTableView{\n" \
        "color: #797979;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "font-size: 12px;\n" \
        "background: #FFF;\n" \
        "}\n" \
        "QHeaderView:section{\n" \
        "background: #FFF;\n" \
        "font-size: 12px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #797979;\n" \
        "border: none;\n" \
        "border-bottom: 1px solid #CCC;\n" \
        "height: 25px;\n" \
        "}\n" \
        "QTableView::item {\n" \
        "border-bottom: 2px solid #CCC;\n" \
        "padding: 2px;\n" \
        "}\n"

        styleLbTitulo = "QLabel{\n" \
        "font-size: 14px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "\n" \
        "border-bottom: 2px solid #A2A2A2\n" \
        "}"

        styleID = "QLineEdit{\n" \
        "background: #CFCFCF;\n" \
        "border: 1px solid #A2A2A2;\n" \
        "color: #000;\n" \
        "font-size: 14px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "\n" \
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
        " }\n" \
        "QComboBox::down-arrow {\n" \
        "     image: url(Images/down.png);\n" \
        " }\n"

        styleLbCampos = "QLabel{\n" \
        "font-size: 12px;\n" \
        "font-family: \"Arial Unicode MS\";\n" \
        "font-weight: bold;\n" \
        "color: #797979\n" \
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

        styleTXWhite = "QLineEdit{\n" \
        "background: #FFF;\n" \
        "border-radius: 2px;\n" \
        "color: #7AB32E;\n" \
        "font: 20px \"Arial\" ;\n" \
        "font-weight: bold\n" \
        "}\n" \
        "QLineEdit:Focus {\n" \
        "border: 1px solid red;\n" \
        "}"

        styleBotaoSalvar = "QPushButton {\n" \
        "background-color: #7AB32E;\n" \
        "color: #FFF\n" \
        " }\n" \
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

        """ Dados Cadastrais """

        # Image
        self.lb_FotoProduto = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FotoProduto.setGeometry(QtCore.QRect(20, 110, 200, 200))
        self.lb_FotoProduto.setStyleSheet("border: 1px solid #A2A2A2;\n")
        self.lb_FotoProduto.setText("")
        self.lb_FotoProduto.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FotoProduto.setObjectName("lb_FotoProduto")

        self.bt_AdicionarImagem = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_AdicionarImagem.setGeometry(QtCore.QRect(190, 280, 25, 25))
        self.bt_AdicionarImagem.setFont(fontArial)
        self.bt_AdicionarImagem.setStyleSheet(styleBotaoSalvar)
        self.bt_AdicionarImagem.setText("")
        self.bt_AdicionarImagem.setObjectName("bt_AdicionarImagem")

        self.bt_DeletarImagem = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_DeletarImagem.setGeometry(QtCore.QRect(190, 280, 25, 25))
        self.bt_DeletarImagem.setFont(fontArial)
        self.bt_DeletarImagem.setStyleSheet(styleBotaoSalvar)
        self.bt_DeletarImagem.setText("")
        self.bt_DeletarImagem.setObjectName("bt_DeletarImagem")

        # codigoBarras é o ID
        self.bt_codigoBarra = QtWidgets.QLabel(self.fr_FormProdutos)
        self.bt_codigoBarra.setGeometry(QtCore.QRect(20, 10, 200, 50))
        self.bt_codigoBarra.setText("")
        self.bt_codigoBarra.setPixmap(QtGui.QPixmap("../Images/CodBarra.png"))
        self.bt_codigoBarra.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_codigoBarra.setObjectName("bt_codigoBarra")

        self.tx_idProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_idProduto.setEnabled(False)
        self.tx_idProduto.setGeometry(QtCore.QRect(20, 85, 200, 25))
        self.tx_idProduto.setStyleSheet(styleID)
        self.tx_idProduto.setText("")
        self.tx_idProduto.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_idProduto.setObjectName("tx_idProduto")

        self.lb_TituloFormProduto = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_TituloFormProduto.setGeometry(QtCore.QRect(250, 10, 730, 30))
        self.lb_TituloFormProduto.setStyleSheet(styleLbTitulo)
        self.lb_TituloFormProduto.setObjectName("lb_TituloFormProduto")

        self.lb_NomeProduto = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_NomeProduto.setGeometry(QtCore.QRect(250, 60, 450, 20))
        self.lb_NomeProduto.setStyleSheet(styleLbCampos)
        self.lb_NomeProduto.setObjectName("lb_NomeProduto")

        self.tx_NomeProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_NomeProduto.setGeometry(QtCore.QRect(250, 85, 450, 25))
        self.tx_NomeProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NomeProduto.setStyleSheet(styleTxCampos)
        self.tx_NomeProduto.setObjectName("tx_NomeProduto")

        self.lb_Descricao = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_Descricao.setGeometry(QtCore.QRect(250, 120, 450, 20))
        self.lb_Descricao.setStyleSheet(styleLbCampos)
        self.lb_Descricao.setObjectName("lb_Descricao")

        self.tx_Descricao = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_Descricao.setGeometry(QtCore.QRect(250, 145, 450, 25))
        self.tx_Descricao.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Descricao.setStyleSheet(styleTxCampos)
        self.tx_Descricao.setObjectName("tx_Descricao")

        self.lb_Categoria = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_Categoria.setGeometry(QtCore.QRect(250, 180, 215, 20))
        self.lb_Categoria.setStyleSheet(styleLbCampos)
        self.lb_Categoria.setObjectName("lb_Categoria")

        self.cb_Categoria = QtWidgets.QComboBox(self.fr_FormProdutos)
        self.cb_Categoria.setGeometry(QtCore.QRect(250, 205, 215, 25))
        self.cb_Categoria.setStyleSheet(styleCbCampos)
        self.cb_Categoria.setObjectName("cb_Categoria")
        self.cb_Categoria.addItem("")

        self.lb_Marca = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_Marca.setGeometry(QtCore.QRect(485, 180, 215, 20))
        self.lb_Marca.setStyleSheet(styleLbCampos)

        self.cb_Marca = QtWidgets.QComboBox(self.fr_FormProdutos)
        self.cb_Marca.setGeometry(QtCore.QRect(485, 205, 215, 25))
        self.cb_Marca.setStyleSheet(styleCbCampos)
        self.cb_Marca.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        # self.cb_Marca.setFrame(False)
        self.cb_Marca.setObjectName("cb_Marca")
        self.cb_Marca.addItem("")

        self.lb_QtdMinimoEstoque = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_QtdMinimoEstoque.setGeometry(QtCore.QRect(250, 240, 215, 20))
        self.lb_QtdMinimoEstoque.setStyleSheet(styleLbCampos)

        self.tx_QtdMinimoEstoque = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_QtdMinimoEstoque.setGeometry(QtCore.QRect(250, 265, 215, 25))
        self.tx_QtdMinimoEstoque.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_QtdMinimoEstoque.setStyleSheet(styleTxCampos)
        self.tx_QtdMinimoEstoque.setPlaceholderText("")
        self.tx_QtdMinimoEstoque.setObjectName("tx_QtdMinimoEstoque")

        self.lb_QtdEstoque = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_QtdEstoque.setGeometry(QtCore.QRect(485, 240, 215, 20))
        self.lb_QtdEstoque.setStyleSheet(styleLbCampos)

        self.tx_QtdEstoque = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_QtdEstoque.setGeometry(QtCore.QRect(485, 265, 215, 25))
        self.tx_QtdEstoque.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_QtdEstoque.setStyleSheet(styleTxCampos)
        self.tx_QtdEstoque.setText("")
        self.tx_QtdEstoque.setPlaceholderText("")
        self.tx_QtdEstoque.setObjectName("tx_QtdEstoque")

        """ Frame Precos """

        self.lb_PrecoTitulo = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_PrecoTitulo.setGeometry(QtCore.QRect(250, 330, 960, 30))
        self.lb_PrecoTitulo.setStyleSheet(styleLbTitulo)
        self.lb_PrecoTitulo.setObjectName("lb_PrecoTitulo")

        self.lb_ValorUnitario = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_ValorUnitario.setGeometry(QtCore.QRect(250, 385, 215, 20))
        self.lb_ValorUnitario.setStyleSheet(styleLbCampos)
        self.lb_ValorUnitario.setObjectName("lb_ValorUnitario")

        self.tx_ValorUnitario = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_ValorUnitario.setGeometry(QtCore.QRect(250, 410, 215, 30))
        self.tx_ValorUnitario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorUnitario.setStyleSheet(styleTxCampos)
        self.tx_ValorUnitario.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_ValorUnitario.setObjectName("tx_ValorUnitario")

        self.lb_TotalEstoque = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_TotalEstoque.setGeometry(QtCore.QRect(485, 385, 215, 20))
        self.lb_TotalEstoque.setStyleSheet(styleLbCampos)
        self.lb_TotalEstoque.setObjectName("lb_ValorTotal")

        self.tx_TotalEstoque = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_TotalEstoque.setGeometry(QtCore.QRect(485, 410, 215, 30))
        self.tx_TotalEstoque.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_TotalEstoque.setStyleSheet(styleTXWhite)
        self.tx_TotalEstoque.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tx_TotalEstoque.setReadOnly(True)
        self.tx_TotalEstoque.setObjectName("tx_ValorTotal")

        """ Frame Actions """

        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\nborder: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")

        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 0, 120, 30))
        self.bt_Voltar.setFont(fontTahoma)
        self.bt_Voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Voltar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Voltar.setStyleSheet(styleBotaoVoltar)
        self.bt_Voltar.setObjectName("bt_Voltar")

        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_Salvar.setGeometry(QtCore.QRect(750, 0, 120, 30))
        self.bt_Salvar.setFont(fontTahoma)
        self.bt_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet(styleBotaoSalvar)
        self.bt_Salvar.setObjectName("bt_Salvar")

        """ End """

        self.translateUiFormProdutos(ct_FormProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormProdutos)
        ct_FormProdutos.setTabOrder(self.tx_idProduto, self.tx_NomeProduto)
        ct_FormProdutos.setTabOrder(self.tx_NomeProduto, self.tx_Descricao)
        ct_FormProdutos.setTabOrder(self.tx_Descricao, self.cb_Categoria)
        ct_FormProdutos.setTabOrder(self.cb_Categoria, self.cb_Marca)
        ct_FormProdutos.setTabOrder(self.cb_Marca, self.tx_QtdMinimoEstoque)
        ct_FormProdutos.setTabOrder(self.tx_QtdMinimoEstoque, self.tx_QtdEstoque)
        ct_FormProdutos.setTabOrder(self.tx_QtdEstoque, self.tx_ValorUnitario)

    def translateUiFormProdutos(self, ct_FormProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormProdutos.setWindowTitle(_translate("ct_FormProdutos", "Frame"))
        self.lb_TituloFormProduto.setText(_translate("ct_FormProdutos", "CADASTRAR PRODUTO"))
        """ Dados Cadastrais """
        self.lb_NomeProduto.setText(_translate("ct_FormProdutos", "NOME"))
        self.lb_Descricao.setText(_translate("ct_FormProdutos", "DESCRIÇÃO"))
        self.lb_Categoria.setText(_translate("ct_FormProdutos", "CATEGORIA"))
        self.cb_Categoria.setItemText(0, _translate("ct_FormProdutos", "SELECIONE"))
        self.lb_Marca.setText(_translate("ct_FormProdutos", "MARCA"))
        self.cb_Marca.setItemText(0, _translate("ct_FormProdutos", "SELECIONE"))
        self.lb_QtdMinimoEstoque.setText(_translate("ct_FormProdutos", "ESTOQUE MÍNIMO"))
        self.lb_QtdEstoque.setText(_translate("ct_FormProdutos", "QUANTIDADE"))
        """ Preco """
        self.lb_PrecoTitulo.setText(_translate("ct_FormProdutos", "PREÇOS"))
        self.lb_ValorUnitario.setText(_translate("ct_FormProdutos", "VALOR UNITÁRIO"))
        self.tx_ValorUnitario.setPlaceholderText(_translate("ct_FormProdutos", "R$ 0.00"))
        self.lb_TotalEstoque.setText(_translate("ct_FormProdutos", "TOTAL"))
        self.tx_TotalEstoque.setPlaceholderText(_translate("ct_FormProdutos", "R$ 0.00"))
        """ Ações """
        self.bt_Voltar.setText(_translate("ct_FormProdutos", "CANCELAR"))
        self.bt_Salvar.setText(_translate("ct_FormProdutos", "SALVAR"))
        self.bt_AdicionarImagem.setToolTip(_translate("ct_FormProdutos", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>"))
        self.bt_DeletarImagem.setToolTip(_translate("ct_FormProdutos", "<html><head/><body><p>Deletar Imagem</p></body></html>"))
