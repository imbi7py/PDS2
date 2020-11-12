# -*- coding: utf-8 -*-
from functools import partial
import re

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon

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
        botao.setIconSize(QSize(30, 30))

    def IconeFlorHome(self, botao, imagem):
        icon = QIcon()
        icon.addPixmap(QPixmap(imagem), QIcon.Normal, QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QSize(500, 300))
