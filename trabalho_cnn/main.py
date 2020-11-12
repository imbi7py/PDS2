# -*- coding: utf-8 -*-
import os
import sys
import random
import webbrowser

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets

from core import Conexao
from Funcoes import Funcao
from home import MainHome
from mainconfig import MainConfig
from mainclassificacao import MainClassificacao
from Views.main import Ui_MainWindow

# Icons
import Images

class Main(QtWidgets.QMainWindow, Ui_MainWindow, MainHome, MainConfig, MainClassificacao, Conexao, Funcao):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # single class to check config...
        self.conexao = Conexao()

        # caminho absoluto ate o diretorio de execucao
        self.caminho = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.inicializarUi(self)

        # Icone dos botoes do Topo
        self.IconeBotaoTopo(self.bt_HomeLogo, self.resourcepath('Images/logoIFSC.png'), True)
        self.IconeBotaoTopo(self.bt_HomeFlor, self.resourcepath('Images/iconcomputer.png'))
        self.IconeBotaoTopo(self.bt_Home, self.resourcepath('Images/home.png'))
        self.IconeBotaoTopo(self.bt_Ajuda, self.resourcepath('Images/ajuda.png'))
        self.IconeBotaoTopo(self.bt_Exit, self.resourcepath('Images/exit.png'))

        # acoes botoes
        self.bt_HomeLogo.clicked.connect(self.janelaHome)
        self.bt_Home.clicked.connect(self.janelaHome)
        self.bt_Ajuda.clicked.connect(self.janelaConfiguracao)

        """ Fim Botoes """
        self.janelaHome()

    def resourcepath(self, relative_path):
        base_path = self.caminho
        return os.path.join(base_path, relative_path)

    """Abrir Janelas: Funcoes para abrir frames limpos"""

    # Main Home
    def janelaHome(self):
        self.LimpaFrame(self.ct_conteudo)
        self.main_home(self.ct_conteudo)

    # Main Config
    def janelaConfiguracao(self):
        self.LimpaFrame(self.ct_conteudo)
        self.mainconfiguracao(self.ct_conteudo)

    # Main Config
    def janelaClassificacao(self):
        self.LimpaFrame(self.ct_conteudo)
        self.mainclassificacao(self.ct_conteudo)

    def checkConfiguration(self):
        print(self.resourcepath('config.ini'))
        if (self.conexao.isConfigurada()):
            self.janelaClassificacao()
        else:
            self.janelaConfiguracao()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
