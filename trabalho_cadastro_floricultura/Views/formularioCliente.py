# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormClientes(object):
    def setFormClientes(self, ct_FormClientes):
        ct_FormClientes.setObjectName("ct_FormClientes")
        ct_FormClientes.resize(1000, 500)
        ct_FormClientes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormClientes.setFrameShadow(QtWidgets.QFrame.Raised)

        self.fr_FormClientes = QtWidgets.QFrame(ct_FormClientes)
        self.fr_FormClientes.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormClientes.setStyleSheet("background: #FFF;\nborder: none")
        self.fr_FormClientes.setObjectName("fr_FormClientes")

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

        styleBotaoCEP = "QPushButton{\n" \
        "background: #7AB32E;\n" \
        "color: #FFF\n" \
        "}\n" \
        "QPushButton:hover{\n" \
        "background-color: #40a286\n" \
        "}"

        styleHTitulo = "QLabel{\n" \
        "font-size: 14px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: normal;\n" \
        "\n" \
        "border-bottom: 2px solid #A2A2A2;\n" \
        "color: #797979\n" \
        "}"

        styleTxTotalHistorico = "QLabel{\n" \
        "font-size: 20px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #277298;\n" \
        "border: none\n" \
        "}"

        styleTotalHistorico = "QLabel{\n" \
        "font-size: 15px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #277298;\n" \
        "border: none\n" \
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

        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Id.setEnabled(False)
        self.tx_Id.setGeometry(QtCore.QRect(20, 10, 50, 30))
        self.tx_Id.setStyleSheet(styleID)
        self.tx_Id.setText("")
        self.tx_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Id.setObjectName("tx_Id")

        self.lb_TituloFormCliente = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_TituloFormCliente.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_TituloFormCliente.setStyleSheet(styleLbTitulo)
        self.lb_TituloFormCliente.setObjectName("lb_TituloFormCliente")

        self.lb_NomeCliente = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_NomeCliente.setGeometry(QtCore.QRect(236, 60, 150, 20))
        self.lb_NomeCliente.setStyleSheet(styleLbCampos)
        self.lb_NomeCliente.setObjectName("lb_NomeCliente")

        self.tx_NomeCliente = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_NomeCliente.setGeometry(QtCore.QRect(236, 85, 190, 25))
        self.tx_NomeCliente.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NomeCliente.setStyleSheet(styleTxCampos)
        self.tx_NomeCliente.setObjectName("tx_NomeCliente")

        self.lb_Sobrenome = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Sobrenome.setGeometry(QtCore.QRect(452, 60, 150, 20))
        self.lb_Sobrenome.setStyleSheet(styleLbCampos)
        self.lb_Sobrenome.setObjectName("lb_Sobrenome")

        self.tx_Sobrenome = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Sobrenome.setGeometry(QtCore.QRect(452, 85, 190, 25))
        self.tx_Sobrenome.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Sobrenome.setStyleSheet(styleTxCampos)
        self.tx_Sobrenome.setObjectName("tx_Sobrenome")

        self.lb_CPF = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_CPF.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_CPF.setStyleSheet(styleLbCampos)
        self.lb_CPF.setObjectName("lb_CPF")

        self.tx_CPF = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_CPF.setGeometry(QtCore.QRect(236, 145, 196, 25))
        self.tx_CPF.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CPF.setStyleSheet(styleTxCampos)
        self.tx_CPF.setPlaceholderText("")
        self.tx_CPF.setObjectName("tx_CPF")

        self.lb_RG = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_RG.setGeometry(QtCore.QRect(452, 120, 190, 20))
        self.lb_RG.setStyleSheet(styleLbCampos)
        self.lb_RG.setObjectName("lb_RG")

        self.tx_RG = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_RG.setGeometry(QtCore.QRect(452, 145, 196, 25))
        self.tx_RG.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_RG.setStyleSheet(styleTxCampos)
        self.tx_RG.setPlaceholderText("")
        self.tx_RG.setObjectName("tx_RG")

        self.lb_Celular = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Celular.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_Celular.setStyleSheet(styleLbCampos)
        self.lb_Celular.setObjectName("lb_Celular")

        self.tx_Celular = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Celular.setGeometry(QtCore.QRect(20, 205, 196, 25))
        self.tx_Celular.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Celular.setStyleSheet(styleTxCampos)
        self.tx_Celular.setPlaceholderText("")
        self.tx_Celular.setObjectName("tx_Celular")

        self.lb_Telefone = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Telefone.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_Telefone.setStyleSheet(styleLbCampos)
        self.lb_Telefone.setObjectName("lb_Telefone")

        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Telefone.setGeometry(QtCore.QRect(236, 205, 196, 25))
        self.tx_Telefone.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Telefone.setStyleSheet(styleTxCampos)
        self.tx_Telefone.setPlaceholderText("")
        self.tx_Telefone.setObjectName("tx_Telefone")

        self.lb_Email = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Email.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_Email.setStyleSheet(styleLbCampos)
        self.lb_Email.setObjectName("lb_Email")

        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Email.setGeometry(QtCore.QRect(452, 205, 196, 25))
        self.tx_Email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Email.setStyleSheet(styleTxCampos)
        self.tx_Email.setPlaceholderText("")
        self.tx_Email.setObjectName("tx_Email")

        self.lb_Observacao = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Observacao.setGeometry(QtCore.QRect(20, 235, 150, 20))
        self.lb_Observacao.setStyleSheet(styleLbCampos)
        self.lb_Observacao.setObjectName("lb_Observacao")

        self.tx_Observacao = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Observacao.setGeometry(QtCore.QRect(20, 260, 630, 25))
        self.tx_Observacao.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Observacao.setStyleSheet(styleTxCampos)
        self.tx_Observacao.setObjectName("tx_Observacao")

        """ Endereco """

        self.lb_EnderecoTitulo = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_EnderecoTitulo.setGeometry(QtCore.QRect(20, 290, 630, 30))
        self.lb_EnderecoTitulo.setStyleSheet(styleHTitulo)
        self.lb_EnderecoTitulo.setObjectName("lb_EnderecoTitulo")

        self.lb_CEP = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_CEP.setGeometry(QtCore.QRect(20, 335, 50, 20))
        self.lb_CEP.setStyleSheet(styleLbCampos)
        self.lb_CEP.setObjectName("lb_CEP")

        self.tx_CEP = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_CEP.setGeometry(QtCore.QRect(20, 360, 100, 25))
        self.tx_CEP.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_CEP.setStyleSheet(styleTxCampos)
        self.tx_CEP.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CEP.setObjectName("tx_CEP")

        self.bt_BuscaCep = QtWidgets.QPushButton(self.fr_FormClientes)
        self.bt_BuscaCep.setGeometry(QtCore.QRect(120, 360, 25, 25))
        self.bt_BuscaCep.setFont(fontArial)
        self.bt_BuscaCep.setStyleSheet(styleBotaoCEP)
        self.bt_BuscaCep.setText("")
        self.bt_BuscaCep.setObjectName("bt_BuscaCep")

        self.lb_Endereco = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Endereco.setGeometry(QtCore.QRect(160, 335, 250, 20))
        self.lb_Endereco.setStyleSheet(styleLbCampos)
        self.lb_Endereco.setObjectName("lb_Endereco")

        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Endereco.setGeometry(QtCore.QRect(160, 360, 400, 25))
        self.tx_Endereco.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Endereco.setStyleSheet(styleTxCampos)
        self.tx_Endereco.setInputMask("")
        self.tx_Endereco.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_Endereco.setPlaceholderText("")
        self.tx_Endereco.setObjectName("tx_Endereco")

        self.lb_Numero = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Numero.setGeometry(QtCore.QRect(580, 335, 50, 20))
        self.lb_Numero.setStyleSheet(styleLbCampos)
        self.lb_Numero.setObjectName("lb_Numero")

        self.tx_Numero = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Numero.setGeometry(QtCore.QRect(580, 360, 70, 25))
        self.tx_Numero.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Numero.setStyleSheet(styleTxCampos)
        self.tx_Numero.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tx_Numero.setInputMask("")
        self.tx_Numero.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_Numero.setPlaceholderText("")
        self.tx_Numero.setObjectName("tx_Numero")

        self.lb_Bairro = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Bairro.setGeometry(QtCore.QRect(20, 390, 120, 20))
        self.lb_Bairro.setStyleSheet(styleLbCampos)
        self.lb_Bairro.setObjectName("lb_Bairro")

        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Bairro.setGeometry(QtCore.QRect(20, 415, 260, 25))
        self.tx_Bairro.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Bairro.setStyleSheet(styleTxCampos)
        self.tx_Bairro.setInputMask("")
        self.tx_Bairro.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_Bairro.setPlaceholderText("")
        self.tx_Bairro.setObjectName("tx_Bairro")

        self.lb_Cidade = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Cidade.setGeometry(QtCore.QRect(300, 390, 120, 20))
        self.lb_Cidade.setStyleSheet(styleLbCampos)
        self.lb_Cidade.setObjectName("lb_Cidade")

        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Cidade.setGeometry(QtCore.QRect(300, 415, 260, 25))
        self.tx_Cidade.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cidade.setStyleSheet(styleTxCampos)
        self.tx_Cidade.setInputMask("")
        self.tx_Cidade.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_Cidade.setPlaceholderText("")
        self.tx_Cidade.setObjectName("tx_Cidade")

        self.lb_Estado = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_Estado.setGeometry(QtCore.QRect(580, 390, 70, 20))
        self.lb_Estado.setStyleSheet(styleLbCampos)
        self.lb_Estado.setObjectName("lb_Estado")

        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Estado.setGeometry(QtCore.QRect(580, 415, 70, 25))
        self.tx_Estado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Estado.setStyleSheet(styleTxCampos)
        self.tx_Estado.setInputMask("")
        self.tx_Estado.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tx_Estado.setPlaceholderText("")
        self.tx_Estado.setObjectName("tx_Estado")

        """ Frame Actions """

        self.fr_BotoesFormClientes = QtWidgets.QFrame(self.fr_FormClientes)
        self.fr_BotoesFormClientes.setGeometry(QtCore.QRect(0, 470, 1000, 30))
        self.fr_BotoesFormClientes.setStyleSheet("background:#E1DFE0;\nborder: none;")
        self.fr_BotoesFormClientes.setObjectName("fr_BotoesFormClientes")

        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormClientes)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 0, 120, 30))
        self.bt_Voltar.setFont(fontTahoma)
        self.bt_Voltar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Voltar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Voltar.setStyleSheet(styleBotaoVoltar)
        self.bt_Voltar.setObjectName("bt_Voltar")

        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormClientes)
        self.bt_Salvar.setGeometry(QtCore.QRect(750, 0, 120, 30))
        self.bt_Salvar.setFont(fontTahoma)
        self.bt_Salvar.setCursor(QtCore.Qt.PointingHandCursor)
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet(styleBotaoSalvar)
        self.bt_Salvar.setObjectName("bt_Salvar")

        """ End """

        self.translateUiFormClientes(ct_FormClientes)
        QtCore.QMetaObject.connectSlotsByName(ct_FormClientes)
        ct_FormClientes.setTabOrder(self.tx_Id, self.tx_NomeCliente)
        ct_FormClientes.setTabOrder(self.tx_NomeCliente, self.tx_Sobrenome)
        ct_FormClientes.setTabOrder(self.tx_Sobrenome, self.tx_CPF)
        ct_FormClientes.setTabOrder(self.tx_CPF, self.tx_RG)
        ct_FormClientes.setTabOrder(self.tx_RG, self.tx_Celular)
        ct_FormClientes.setTabOrder(self.tx_Celular, self.tx_Telefone)
        ct_FormClientes.setTabOrder(self.tx_Telefone, self.tx_Email)
        ct_FormClientes.setTabOrder(self.tx_Email, self.tx_Observacao)
        ct_FormClientes.setTabOrder(self.tx_Observacao, self.tx_CEP)
        ct_FormClientes.setTabOrder(self.tx_CEP, self.bt_BuscaCep)
        ct_FormClientes.setTabOrder(self.bt_BuscaCep, self.tx_Endereco)
        ct_FormClientes.setTabOrder(self.tx_Endereco, self.tx_Numero)
        ct_FormClientes.setTabOrder(self.tx_Numero, self.tx_Bairro)
        ct_FormClientes.setTabOrder(self.tx_Bairro, self.tx_Cidade)
        ct_FormClientes.setTabOrder(self.tx_Cidade, self.tx_Estado)

    def translateUiFormClientes(self, ct_FormClientes):
        ct_FormClientes.setWindowTitle(QtWidgets.QApplication.translate("ct_FormClientes", "Frame", None, -1))
        """ Dados Cadastrais """
        self.lb_TituloFormCliente.setText(QtWidgets.QApplication.translate("ct_FormClientes", "FICHA CADASTRAL CLIENTE", None, -1))
        self.lb_NomeCliente.setText(QtWidgets.QApplication.translate("ct_FormClientes", "NOME", None, -1))
        # self.tx_NomeCliente.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "NOME", None, -1))
        self.lb_Sobrenome.setText(QtWidgets.QApplication.translate("ct_FormClientes", "SOBRENOME", None, -1))
        # self.tx_Sobrenome.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "SOBRENOME", None, -1))
        self.lb_CPF.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CPF", None, -1))
        self.tx_CPF.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "000.000.000-00", None, -1))
        self.lb_RG.setText(QtWidgets.QApplication.translate("ct_FormClientes", "RG", None, -1))
        self.tx_RG.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "0.000.000", None, -1))
        self.lb_Celular.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CELULAR", None, -1))
        self.tx_Celular.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "(00) 00000-0000", None, -1))
        # self.tx_Celular.setText(QtWidgets.QApplication.translate("ct_FormClientes", "() -", None, -1))
        self.lb_Telefone.setText(QtWidgets.QApplication.translate("ct_FormClientes", "TELEFONE", None, -1))
        self.tx_Telefone.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "(00) 0000-0000", None, -1))
        self.lb_Email.setText(QtWidgets.QApplication.translate("ct_FormClientes", "Email", None, -1))
        # self.tx_Email.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "EMAIL", None, -1))
        self.lb_Observacao.setText(QtWidgets.QApplication.translate("ct_FormClientes", "OBSERVAÇÃO", None, -1))
        # self.tx_Observacao.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "Observação", None, -1))
        """ Endereco """
        self.lb_EnderecoTitulo.setText(QtWidgets.QApplication.translate("ct_FormClientes", "ENDEREÇO", None, -1))
        self.lb_CEP.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CEP", None, -1))
        self.tx_CEP.setInputMask(QtWidgets.QApplication.translate("ct_FormClientes", "99999-999", None, -1))
        # self.tx_CEP.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "123456789", None, -1))
        self.lb_Endereco.setText(QtWidgets.QApplication.translate("ct_FormClientes", "ENDEREÇO", None, -1))
        # self.tx_Endereco.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "ENDEREÇO", None, -1))
        self.lb_Numero.setText(QtWidgets.QApplication.translate("ct_FormClientes", "Nº", None, -1))
        # self.tx_Numero.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "NÚMERO CASA", None, -1))
        self.lb_Bairro.setText(QtWidgets.QApplication.translate("ct_FormClientes", "BAIRRO", None, -1))
        # self.tx_Bairro.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "BAIRRO", None, -1))
        self.lb_Cidade.setText(QtWidgets.QApplication.translate("ct_FormClientes", "CIDADE", None, -1))
        # self.tx_Cidade.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "CIDADE", None, -1))
        self.lb_Estado.setText(QtWidgets.QApplication.translate("ct_FormClientes", "ESTADO", None, -1))
        # self.tx_Estado.setPlaceholderText(QtWidgets.QApplication.translate("ct_FormClientes", "ESTADO", None, -1))
        """ Ações """
        self.bt_Voltar.setText(QtWidgets.QApplication.translate("ct_FormClientes", "VOLTAR", None, -1))
        self.bt_Salvar.setText(QtWidgets.QApplication.translate("ct_FormClientes", "SALVAR", None, -1))

