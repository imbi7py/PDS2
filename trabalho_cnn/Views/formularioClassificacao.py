# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ct_FormClassificacao(object):
    def setFormClassificacao(self, ct_FormClassificacao):
        ct_FormClassificacao.setObjectName("ct_FormClassificacao")
        ct_FormClassificacao.resize(1000, 700)
        ct_FormClassificacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ct_FormClassificacao.setFrameShadow(QtWidgets.QFrame.Raised)

        self.fr_FormClassificacao = QtWidgets.QFrame(ct_FormClassificacao)
        self.fr_FormClassificacao.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.fr_FormClassificacao.setStyleSheet("background: #FFF;\nborder: none")
        self.fr_FormClassificacao.setObjectName("fr_FormClassificacao")

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
        self.lb_FotoClassificacao = QtWidgets.QLabel(self.fr_FormClassificacao)
        self.lb_FotoClassificacao.setGeometry(QtCore.QRect(20, 60, 300, 250))
        self.lb_FotoClassificacao.setStyleSheet("border: 1px solid #A2A2A2;\n")
        self.lb_FotoClassificacao.setText("")
        self.lb_FotoClassificacao.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FotoClassificacao.setObjectName("lb_FotoClassificacao")

        self.bt_AdicionarImagem = QtWidgets.QPushButton(self.fr_FormClassificacao)
        self.bt_AdicionarImagem.setGeometry(QtCore.QRect(280, 275, 30, 30))
        self.bt_AdicionarImagem.setFont(fontArial)
        self.bt_AdicionarImagem.setStyleSheet(styleBotaoSalvar)
        self.bt_AdicionarImagem.setText("")
        self.bt_AdicionarImagem.setObjectName("bt_AdicionarImagem")

        self.bt_DeletarImagem = QtWidgets.QPushButton(self.fr_FormClassificacao)
        self.bt_DeletarImagem.setGeometry(QtCore.QRect(280, 275, 30, 30))
        self.bt_DeletarImagem.setFont(fontArial)
        self.bt_DeletarImagem.setStyleSheet(styleBotaoSalvar)
        self.bt_DeletarImagem.setText("")
        self.bt_DeletarImagem.setObjectName("bt_DeletarImagem")

        self.lb_ImagemTitulo = QtWidgets.QLabel(self.fr_FormClassificacao)
        self.lb_ImagemTitulo.setGeometry(QtCore.QRect(350, 50, 630, 30))
        self.lb_ImagemTitulo.setStyleSheet(styleLbTitulo)
        self.lb_ImagemTitulo.setObjectName("lb_ImagemTitulo")

        self.lb_ImagemClassificacao = QtWidgets.QLabel(self.fr_FormClassificacao)
        self.lb_ImagemClassificacao.setGeometry(QtCore.QRect(350, 100, 450, 60))
        self.lb_ImagemClassificacao.setStyleSheet(styleLbCampos)
        self.lb_ImagemClassificacao.setObjectName("lb_ImagemClassificacao")

        self.lb_Resultado = QtWidgets.QLabel(self.fr_FormClassificacao)
        self.lb_Resultado.setGeometry(QtCore.QRect(350, 250, 450, 60))
        self.lb_Resultado.setStyleSheet(styleLbCampos)
        self.lb_Resultado.setObjectName("lb_Resultado")
        """ Actions """

        self.bt_Salvar = QtWidgets.QPushButton(self.fr_FormClassificacao)
        self.bt_Salvar.setGeometry(QtCore.QRect(450, 330, 100, 40))
        self.bt_Salvar.setFont(fontTahoma)
        self.bt_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet(styleBotaoSalvar)
        self.bt_Salvar.setObjectName("bt_Salvar")

        """ End """

        self.translateUiFormClassificacao(ct_FormClassificacao)
        QtCore.QMetaObject.connectSlotsByName(ct_FormClassificacao)

    def translateUiFormClassificacao(self, ct_FormClassificacao):
        _translate = QtCore.QCoreApplication.translate
        ct_FormClassificacao.setWindowTitle(_translate("ct_FormClassificacao", "Frame"))
        """ RNA """
        self.lb_ImagemTitulo.setText(_translate("lb_ImagemTitulo", "CLASSIFICAR RAIO-X"))
        self.lb_ImagemClassificacao.setText(_translate("lb_ImagemClassificacao", "O sistema classifica imagens de exames de raio-X.\nAo lado selecione uma imagem para classificacao e o sistema\nidentifica se é um caso de Pneumonia ou nao."))
        self.lb_Resultado.setText(_translate("lb_Resultado", "Resultado: "))
        """ Ações """
        self.bt_Salvar.setText(_translate("bt_Salvar", "Executar"))
        self.bt_AdicionarImagem.setToolTip(_translate("bt_AdicionarImagem", "<html><head/><body><p>Add Imagem</p></body></html>"))
        self.bt_DeletarImagem.setToolTip(_translate("bt_DeletarImagem", "<html><head/><body><p>Deletar Imagem</p></body></html>"))

