# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormConfig(object):
    def setFormConfig(self, ct_FormConfig):
        ct_FormConfig.setObjectName("ct_FormConfig")
        ct_FormConfig.resize(1000, 700)
        ct_FormConfig.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormConfig.setFrameShadow(QtWidgets.QFrame.Raised)

        self.fr_FormConfig = QtWidgets.QFrame(ct_FormConfig)
        self.fr_FormConfig.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.fr_FormConfig.setStyleSheet("background: #FFF;\nborder: none")
        self.fr_FormConfig.setObjectName("fr_FormConfig")

        styleLbTitulo = "QLabel{\n" \
        "font-size: 14px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "\n" \
        "border-bottom: 2px solid #A2A2A2\n" \
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
        self.lb_FotoConfig = QtWidgets.QLabel(self.fr_FormConfig)
        self.lb_FotoConfig.setGeometry(QtCore.QRect(20, 60, 300, 250))
        self.lb_FotoConfig.setStyleSheet("border: 1px solid #A2A2A2;\n")
        self.lb_FotoConfig.setText("")
        self.lb_FotoConfig.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FotoConfig.setObjectName("lb_FotoConfig")

        self.lb_RNATitulo = QtWidgets.QLabel(self.fr_FormConfig)
        self.lb_RNATitulo.setGeometry(QtCore.QRect(350, 50, 630, 30))
        self.lb_RNATitulo.setStyleSheet(styleLbTitulo)
        self.lb_RNATitulo.setObjectName("lb_RNATitulo")

        self.lb_RNAConfig = QtWidgets.QLabel(self.fr_FormConfig)
        self.lb_RNAConfig.setGeometry(QtCore.QRect(350, 100, 450, 20))
        self.lb_RNAConfig.setStyleSheet(styleLbCampos)
        self.lb_RNAConfig.setObjectName("lb_RNAConfig")

        self.tx_RNAConfig = QtWidgets.QLineEdit(self.fr_FormConfig)
        self.tx_RNAConfig.setGeometry(QtCore.QRect(350, 125, 375, 25))
        self.tx_RNAConfig.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_RNAConfig.setStyleSheet(styleTxCampos)
        self.tx_RNAConfig.setObjectName("tx_RNAConfig")

        self.bt_AdicionarRNA = QtWidgets.QPushButton(self.fr_FormConfig)
        self.bt_AdicionarRNA.setGeometry(QtCore.QRect(730, 125, 25, 25))
        self.bt_AdicionarRNA.setFont(fontArial)
        self.bt_AdicionarRNA.setStyleSheet(styleBotaoSalvar)
        self.bt_AdicionarRNA.setText("")
        self.bt_AdicionarRNA.setObjectName("bt_AdicionarRNA")

        """ Pesos """

        self.lb_PesosTitulo = QtWidgets.QLabel(self.fr_FormConfig)
        self.lb_PesosTitulo.setGeometry(QtCore.QRect(350, 200, 630, 30))
        self.lb_PesosTitulo.setStyleSheet(styleLbTitulo)
        self.lb_PesosTitulo.setObjectName("lb_PesosTitulo")

        self.lb_PesosConfig = QtWidgets.QLabel(self.fr_FormConfig)
        self.lb_PesosConfig.setGeometry(QtCore.QRect(350, 255, 450, 20))
        self.lb_PesosConfig.setStyleSheet(styleLbCampos)
        self.lb_PesosConfig.setObjectName("lb_PesosConfig")

        self.tx_PesosConfig = QtWidgets.QLineEdit(self.fr_FormConfig)
        self.tx_PesosConfig.setGeometry(QtCore.QRect(350, 280, 375, 25))
        self.tx_PesosConfig.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_PesosConfig.setStyleSheet(styleTxCampos)
        self.tx_PesosConfig.setObjectName("tx_PesosConfig")

        self.bt_AdicionarPesos = QtWidgets.QPushButton(self.fr_FormConfig)
        self.bt_AdicionarPesos.setGeometry(QtCore.QRect(730, 280, 25, 25))
        self.bt_AdicionarPesos.setFont(fontArial)
        self.bt_AdicionarPesos.setStyleSheet(styleBotaoSalvar)
        self.bt_AdicionarPesos.setText("")
        self.bt_AdicionarPesos.setObjectName("bt_AdicionarPesos")

        """ Actions """

        self.bt_Salvar = QtWidgets.QPushButton(self.fr_FormConfig)
        self.bt_Salvar.setGeometry(QtCore.QRect(450, 330, 100, 40))
        self.bt_Salvar.setFont(fontTahoma)
        self.bt_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet(styleBotaoSalvar)
        self.bt_Salvar.setObjectName("bt_Salvar")

        """ End """

        self.translateUiFormConfig(ct_FormConfig)
        QtCore.QMetaObject.connectSlotsByName(ct_FormConfig)
        ct_FormConfig.setTabOrder(self.tx_RNAConfig, self.tx_PesosConfig)

    def translateUiFormConfig(self, ct_FormConfig):
        _translate = QtCore.QCoreApplication.translate
        ct_FormConfig.setWindowTitle(_translate("ct_FormConfig", "Frame"))
        """ RNA """
        self.lb_RNATitulo.setText(_translate("lb_RNATitulo", "CONFIGURAR RNA"))
        self.lb_RNAConfig.setText(_translate("lb_RNAConfig", "Abaixo seleciona-se o arquivo responsável pela configuração da Rede Neural:"))
        self.tx_RNAConfig.setText(_translate("tx_RNAConfig", "Selecione a RNA em .json"))
        """ Pesos """
        self.lb_PesosTitulo.setText(_translate("lb_PesosTitulo", "CONFIGURAR PESOS"))
        self.lb_PesosConfig.setText(_translate("lb_PesosConfig", "Abaixo seleciona-se o arquivo responsável pelos pesos da Rede Neural:"))
        self.tx_PesosConfig.setText(_translate("tx_PesosConfig", "Selecione os pesos em .h5"))
        """ Ações """
        self.bt_Salvar.setText(_translate("bt_Salvar", "SALVAR"))
        self.bt_AdicionarRNA.setText(_translate("bt_AdicionarRNA", "..."))
        self.bt_AdicionarPesos.setText(_translate("bt_AdicionarPesos", "..."))
