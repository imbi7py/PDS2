# -*- coding: utf-8 -*-

#
# mainprodutos is responsable for managing the Product information in the GUI
#

import re
import json
import os

from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Views.formularioConfig import Ui_ct_FormConfig

class MainConfig(Ui_ct_FormConfig):
    # funcao junta GUI e dados para janela de Config da RNA
    def mainconfiguracao(self, frame):
        super(MainConfig, self).setFormConfig(frame)
        # self.LimpaFrame(frame)
        self.fr_FormConfig.show()
        self.lb_FotoConfig.setPixmap(QPixmap(self.resourcepath("Images/cerebro.jpg")).scaledToWidth(
            250, Qt.TransformationMode(Qt.FastTransformation)))

        self.bt_AdicionarRNA.clicked.connect(self.UploadRNA)
        self.bt_AdicionarPesos.clicked.connect(self.UploadPesos)
        self.bt_Salvar.clicked.connect(self.SalvaConfig)

        if(self.conexao.isConfigurada()):
            self.tx_RNAConfig.setText(self.conexao.pathRNA)
            self.tx_PesosConfig.setText(self.conexao.pathPesos)

    # Cadastro Config
    def SalvaConfig(self):
        pathRNA = self.tx_RNAConfig.text()
        pathPesos = self.tx_PesosConfig.text()

        if(pathRNA == "" or pathPesos == ""):
            msg = QMessageBox()
            msg.setWindowTitle("Alerta de Arquivo")
            msg.setText("Arquivo de RNA e de Peso devem ser selecionados")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok);
            returnValue = msg.exec()
        elif(self.ValidaFile(pathRNA) == False or self.ValidaFile(pathPesos) == False):
            return
        else:
            self.conexao.pathRNA = pathRNA
            self.conexao.pathPesos = pathPesos
            self.conexao.salvar()
            print("passou")
            self.janelaClassificacao()

    def UploadRNA(self):
        Dialog = QFileDialog()
        Dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        filename = Dialog.getOpenFileName(self, "Selecionar JSON", "", "JSON files (*.json)")[0]
        retorno = self.ValidaFile(filename, True)

    def UploadPesos(self):
        Dialog = QFileDialog()
        Dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        filename = Dialog.getOpenFileName(self, "Selecionar h5", "", "h5 files (*.h5)")[0]
        retorno = self.ValidaFile(filename)

    def ValidaFile(self, filename, isJSON=False):
        texto = ""
        if (os.path.exists(filename)):
            if (isJSON == True):
                arquivo = open(filename, 'r')
                estrutura_rede = arquivo.read()
                arquivo.close()

                try:
                    parsed = json.loads(estrutura_rede)
                    texto = json.dumps(parsed, indent=4, sort_keys=True)
                    self.tx_RNAConfig.setText(filename)
                    return True
                except ValueError as e:
                    msg = QMessageBox()
                    msg.setWindowTitle("Alerta de Arquivo")
                    msg.setText("Erro ao carregar JSON file.")
                    msg.setInformativeText("nome de arquivo: %s" % filename)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok);
                    returnValue = msg.exec()
                    return False
            else:
                self.tx_PesosConfig.setText(filename)
                return True
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Alerta de Arquivo")
            msg.setText("Arquivo selecionado é inexistente.")
            msg.setInformativeText("nome de arquivo: %s" % filename)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok);
            returnValue = msg.exec()
            return False

