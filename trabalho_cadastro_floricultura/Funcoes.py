# -*- coding: utf-8 -*-
from functools import partial
import re

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon

from pycep_correios import consultar_cep
from pycep_correios.excecoes import ExcecaoPyCEPCorreios

class Funcao(object):
    def LimpaFrame(self, frame):
        for i in range(len(frame.children())):
            frame.children()[i].deleteLater()

    def DesativaBotao(self, frame, botao):
        for filho in frame.findChildren(QPushButton):
            filho.setEnabled(True)
        botao.setEnabled(False)

    def IconeBotaoTopo(self, botao, imagem, isLogo=False):
        icon = QIcon()
        icon.addPixmap(QPixmap(imagem),
                       QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        if isLogo == False:
            botao.setIconSize(QSize(50, 35))
        else:
            botao.setIconSize(QSize(150, 70))

    def IconeBotaoMenu(self, botao, imagem):
        icon = QIcon()
        icon.addPixmap(QPixmap(imagem),
                       QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QSize(25, 25))

    def IconeFlorHome(self, botao, imagem):
        icon = QIcon()
        icon.addPixmap(QPixmap(imagem), QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QSize(250, 250))

    # Formatando numero de telefone as tabelas
    def formatoNumTelefone(self, telefone):
        if telefone:
            telefone = re.sub('[^0-9]+', '', telefone)
            if len(telefone) == 11:
                formato = re.sub('(\d{2})(\d{5})(\d{4})',
                                 r'(\1) \2-\3', telefone)
            elif len(telefone) == 10:
                formato = re.sub('(\d{2})(\d{4})(\d{4})',
                                 r'(\1) \2-\3', telefone)
            else:
                formato = ""
        else:
            formato = ""
        return formato

    # buscar Cep
    def buscarCepCliente(self):
        cep = self.tx_CEP.text()
        try:
            busca = consultar_cep(cep)
            self.tx_Endereco.setText(busca['end'])
            self.tx_Bairro.setText(busca['bairro'])
            self.tx_Cidade.setText(busca['cidade'])
            self.tx_Estado.setText(busca['uf'])
            self.tx_Numero.setFocus()
        except ExcecaoPyCEPCorreios as exc:
            self.tx_Endereco.setText(exc.message)
