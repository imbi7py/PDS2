# -*- coding: utf-8 -*-
import os
import sys
import random
import webbrowser

from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets

from Crud.ConectorDB import Conexao
from Crud.CreateInfra import CreateDb

from Funcoes import Funcao
from home import MainHome
from mainclientes import MainClientes
from mainprodutos import MainProdutos
from mainvendas import MainVendas
from Views.main import Ui_MainWindow

# Icons
import Images

class Main(QtWidgets.QMainWindow, Ui_MainWindow, MainHome, MainProdutos,
           MainVendas, MainClientes, Funcao):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        # caminho absoluto ate o diretorio de execucao
        self.caminho = os.path.abspath(os.path.dirname(sys.argv[0]))

        Criar = CreateDb()
        Criar.createDB()
        Criar.tabelas()

        self.inicializarUi(self)
        self.centralizarNaTela()

        # Icone dos botoes do Topo
        self.IconeBotaoTopo(self.bt_HomeLogo, self.resourcepath('Images/logoIFSC.png'), True)
        self.IconeBotaoTopo(self.bt_HomeFlor, self.resourcepath('Images/iconeFloricultura.png'))
        self.IconeBotaoTopo(self.bt_Home, self.resourcepath('Images/home.png'))
        self.IconeBotaoTopo(self.bt_Ajuda, self.resourcepath('Images/ajuda.png'))
        self.IconeBotaoTopo(self.bt_Exit, self.resourcepath('Images/exit.png'))
        # Icone botoes do menu
        self.IconeBotaoMenu(self.bt_MainVendas, self.resourcepath('Images/vendas.png'))
        self.IconeBotaoMenu(self.bt_MainProdutos, self.resourcepath('Images/produtos.png'))
        self.IconeBotaoMenu(self.bt_MainClientes, self.resourcepath('Images/clientes.png'))

        # acoes botoes
        self.bt_HomeLogo.clicked.connect(self.janelaHome)
        self.bt_Home.clicked.connect(self.janelaHome)
        self.bt_Ajuda.clicked.connect(self.janelaHome)

        self.bt_MainProdutos.clicked.connect(self.janelaProdutos)
        self.bt_MainVendas.clicked.connect(self.janelaVendas)
        self.bt_MainClientes.clicked.connect(self.janelaClientes)
        """ Fim Botoes """
        self.janelaHome()

    def resourcepath(self, relative_path):
        base_path = self.caminho
        return os.path.join(base_path, relative_path)

    def centralizarNaTela(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    """Abrir Janelas: Funcoes para abrir frames limpos"""

    # Main Home
    def janelaHome(self):
        self.LimpaFrame(self.ct_conteudo)
        self.main_home(self.ct_conteudo)

    # Main Produtos
    def janelaProdutos(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_MainProdutos)
        self.mainprodutos(self.ct_conteudo)

    # Main Vendas
    def janelaVendas(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_MainVendas)
        self.mainvendas(self.ct_conteudo)

    # Main Cliente
    def janelaClientes(self):
        self.LimpaFrame(self.ct_conteudo)
        self.DesativaBotao(self.wd_menu, self.bt_MainClientes)
        self.mainclientes(self.ct_conteudo)

    """ Fim Abrir Janelas """

    """ Organizar tabela """

    # Dados tabela alinhado ao centrol
    def alinharDadosTabela(self, tabela, row, col, data):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignJustify |
                              Qt.AlignHCenter | Qt.AlignVCenter)
        item.setFlags(Qt.NoItemFlags)
        item.setText(data)
        tabela.setItem(row, col, item)

    # Dados tabela alinhado a esquerda
    def alinharDadosTabelaEsquerda(self, tabela, row, col, data):
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(Qt.AlignJustify |
                              Qt.AlignLeft | Qt.AlignVCenter)
        item.setFlags(Qt.NoItemFlags)
        item.setText(data)
        tabela.setItem(row, col, item)

    # Botao Edicao linha tabela
    def botaoTabela(self, tabela, row, col, funcao, bg):
        item = QtWidgets.QPushButton()
        item.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        item.setFocusPolicy(Qt.NoFocus)
        item.setFlat(Qt.NoItemFlags)
        # preparando estilo e texto
        item.setStyleSheet("QPushButton{\n"
                           "background-color: #7AB32E;\n"
                           "border-radius: 2px;\n"
                           "padding: 2px;\n"
                           "color: #FFF;\n"
                           "font: 10px \"Tahoma\" Bold\n"
                           "}\n"
                           "QPushButton:hover{\n"
                           "background-color: #40a286\n"
                           "}")
        item.setText("EDITAR")
        # icone botao
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap(
            self.resourcepath('Images/editar.png')),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icone)
        tabela.setCellWidget(row, col, item)
        # funcao ao clicar
        item.clicked.connect(funcao)

    # Botão Remove Item tabela Venda
    def botaoRemoveItem(self, tabela, row, col, funcao, bg):
        item = QtWidgets.QPushButton()
        item.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        item.setFocusPolicy(Qt.NoFocus)
        item.setFlat(Qt.NoItemFlags)
        item.setStyleSheet("QPushButton{\n"
                           "background-color: " + bg + ";\n"
                           "border-radius: 2px;\n"
                           "padding: 2px;\n"
                           "}\n"
                           "QPushButton:hover{\n"
                           "background-color: #40a286\n"
                           "}")
        item.setText("")
        # icone botao
        icone = QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap(self.resourcepath('Images/edit-delete.png')),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icone)
        tabela.setCellWidget(row, col, item)
        # funcao ao clicar
        item.clicked.connect(funcao)

    # Texto grande Valor Produtos na tabela
    def SetValorTable(self, tabela, row, col, valor):
        item = QtWidgets.QLabel()
        item.setAlignment(
            Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        item.setMargin(0)
        item.setStyleSheet('background: #FFF')
        html = ("""
                <span style="font-family:'Arial'; font-size:30px;
                font-weight: bold;"> <span style="font-size: 12px">R$</span> {}</span><br/>
                """).format(valor)
        item.setText(html)
        tabela.setCellWidget(row, col, item)

    # Formata ate 2 informacoes em 1 celula da tabela
    def SetFormataDadosPessoaisTabela(self, tabela, row, col, elemento1, elemento2):
        item = QtWidgets.QLabel()
        item.setAlignment(Qt.AlignLeading | Qt.AlignLeft |
                          Qt.AlignVCenter)
        item.setIndent(3)
        item.setMargin(0)
        item.setStyleSheet('background: #FFF')
        html = (("""
                <span style="font-family:Arial; font-size:13px; ">{}</span><br/>
                <span style="font-family:Arial; font-size:10px;">{}</span>
                """
                 )).format(elemento1, elemento2)
        item.setText(html)
        tabela.setCellWidget(row, col, item)

    # texto quantidade e cor faltando produtos tabela Produto
    def SetTabelaStatusEstoque(self, tabela, row, col, qtde, cor):
        item = QtWidgets.QLabel()
        item.setAlignment(
            Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        item.setMargin(0)
        item.setStyleSheet('background: #FFF')
        html = ("""
                <span style="font-family:'Arial'; font-size:30px;
                font-weight: bold;color:{} ">{}</span><br/>
                """).format(cor, qtde)
        item.setText(html)
        tabela.setCellWidget(row, col, item)

    # Texto ID tabelas
    def SetTabelaID(self, tabela, row, col, id):
        item = QtWidgets.QLabel()
        item.setAlignment(
            Qt.AlignLeading | Qt.AlignHCenter | Qt.AlignVCenter)
        item.setMargin(0)
        item.setStyleSheet('background: #FFF;')
        html = ("""
               <span style="font-family:'Arial'; font-size:30px; 
               font-weight: bold;color:#7AB32E ">{}</span><br/>
               """).format(id)
        item.setText(html)
        tabela.setCellWidget(row, col, item)

    # Retorna cor status para quantidade abaixo do minimo
    def GetCorStatusEstoque(self, qtde, minimo):
        if qtde > minimo:
            cor = "#7AB32E"
        elif qtde <= minimo:
            cor = "#e69822"
        else:
            cor = "red"
        return cor

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
