# -*- coding: utf-8 -*-

#
# mainprodutos is responsable for managing the Product information in the GUI
#

import re
import os

from functools import partial

import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Views.formularioClassificacao import Ui_ct_FormClassificacao

class MainClassificacao(Ui_ct_FormClassificacao):
    # funcao junta GUI e dados para janela de Classificacao da RNA
    def mainclassificacao(self, frame):
        super(MainClassificacao, self).setFormClassificacao(frame)
        # self.LimpaFrame(frame)
        self.fr_FormClassificacao.show()

        self.IconeBotaoMenu(self.bt_AdicionarImagem, self.resourcepath('Images/edit-add.png'))
        self.IconeBotaoMenu(self.bt_DeletarImagem, self.resourcepath('Images/edit-delete.png'))

        self.bt_DeletarImagem.setHidden(True)

        self.bt_AdicionarImagem.clicked.connect(self.UploadImagem)
        self.bt_DeletarImagem.clicked.connect(self.DeleteImagem)
        self.bt_Salvar.clicked.connect(self.SalvaClassificacao)

    # Cadastro Classificacao
    def SalvaClassificacao(self):
        if (os.path.exists(self.conexao.pathRNA) == False or os.path.exists(self.conexao.pathPesos) == False):
            return
        else:
            arquivo = open(self.conexao.pathRNA, 'r')
            self.conexao.estrutura_rede = arquivo.read()
            arquivo.close()

            self.conexao.classificador = model_from_json(self.conexao.estrutura_rede)
            self.conexao.classificador.load_weights(self.conexao.pathPesos)
            imagem_teste = image.load_img(self.path_imagem, target_size = (64,64))

            #alterar o formato da imagem de teste
            imagem_teste = image.img_to_array(imagem_teste)


            #alterando o formato para o tensor flow adicionando mais uma coluna
            imagem_teste = np.expand_dims(imagem_teste, axis = 0)

            #realizado essas configurações já podemos realizar a previsão
            print("1")
            previsao = self.conexao.classificador.predict(imagem_teste)
            print("2")
            #retornando false para cachorro e verdadeiro para gato
            print("predicao em pontos: ", previsao)
            previsao = (previsao > 0.5)
            print("predicao em boolean: ", previsao)
            if(previsao[0] == True):
                self.lb_Resultado.setText("Resultado: Pneumonia")
            else:
                self.lb_Resultado.setText("Resultado: Caso Normal")

    def UploadImagem(self):
        Dialog = QFileDialog()
        Dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        filename = Dialog.getOpenFileName(self, "Selecionar Imagem", "", "Image files (*.jpeg *.jpg *.png)")[0]

        self.path_imagem = filename
        self.lb_FotoClassificacao.setPixmap(QPixmap(filename).scaledToWidth(
            200, Qt.TransformationMode(Qt.FastTransformation)))
        self.bt_AdicionarImagem.setHidden(True)
        self.bt_DeletarImagem.setVisible(True)

    def DeleteImagem(self):
        self.lb_FotoClassificacao.clear()
        self.bt_DeletarImagem.setHidden(True)
        self.bt_AdicionarImagem.setVisible(True)

