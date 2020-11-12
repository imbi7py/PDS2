# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def inicializarUi(self, MainWindow):
        # tamanho window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        # fonte window
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        # estilo window
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "background: 0 0 no-repeat #e9ebee\n"
                                 "}\n")

        # font para botoes janelas
        fontSegoe = QtGui.QFont()
        fontSegoe.setFamily("Segoe UI")
        fontSegoe.setPointSize(13)

        fontSansSerif9 = QtGui.QFont()
        fontSansSerif9.setFamily("Sans Serif")
        fontSansSerif9.setPointSize(9)

        fontArial12 = QtGui.QFont()
        fontArial12.setFamily("Arial")
        fontArial12.setPointSize(12)

        # estilo para botoes menu superior
        styleSuperior = "QPushButton {\n" \
            "     border: none;\n" \
            "     color: #FFF\n" \
            "}\n" \
            "QPushButton:hover {\n" \
            "     background: #e9ebee\n" \
            "}"

        # widget centro
        self.centralwidget=QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        """ Comeco Menu Topo"""

        # widget topo: menu superior
        self.wd_topo=QtWidgets.QWidget(self.centralwidget)
        self.wd_topo.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        # size policy
        sizePolicy=QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.wd_topo.sizePolicy().hasHeightForWidth())
        self.wd_topo.setSizePolicy(sizePolicy)
        # estilo
        self.wd_topo.setStyleSheet("background: #FFF")
        self.wd_topo.setObjectName("wd_topo")

        # botao ir ao home
        self.bt_HomeLogo = QtWidgets.QPushButton(self.wd_topo)
        self.bt_HomeLogo.setGeometry(QtCore.QRect(5, 5, 150, 50))
        self.bt_HomeLogo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_HomeLogo.setStyleSheet(styleSuperior)
        self.bt_HomeLogo.setText("")
        self.bt_HomeLogo.setFlat(True)
        self.bt_HomeLogo.setObjectName("bt_HomeLogo")

        # botao ir ao home
        self.bt_HomeFlor = QtWidgets.QPushButton(self.wd_topo)
        self.bt_HomeFlor.setGeometry(QtCore.QRect(650, 5, 50, 50))
        self.bt_HomeFlor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_HomeFlor.setStyleSheet(styleSuperior)
        self.bt_HomeFlor.setText("")
        self.bt_HomeFlor.setFlat(True)
        self.bt_HomeFlor.setObjectName("bt_HomeFlor")

        # primeira msg no bem vindo
        self.lb_BemVindo = QtWidgets.QLabel(self.wd_topo)
        self.lb_BemVindo.setGeometry(QtCore.QRect(700, 15, 100, 20))
        font = fontSansSerif9
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_BemVindo.setFont(font)
        self.lb_BemVindo.setStyleSheet("color: #000")
        self.lb_BemVindo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_BemVindo.setObjectName("lb_BemVindo")

        # segunda msg no bem vindo
        self.lb_BemVindo2 = QtWidgets.QLabel(self.wd_topo)
        self.lb_BemVindo2.setGeometry(QtCore.QRect(700, 30, 150, 20))
        self.lb_BemVindo2.setFont(fontSansSerif9)
        self.lb_BemVindo2.setStyleSheet("color: #000")
        self.lb_BemVindo2.setText("")
        self.lb_BemVindo2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_BemVindo2.setObjectName("lb_BemVindo2")

        # botao home
        self.bt_Home = QtWidgets.QPushButton(self.wd_topo)
        self.bt_Home.setGeometry(QtCore.QRect(850, 5, 50, 50))
        self.bt_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Home.setStyleSheet(styleSuperior)
        self.bt_Home.setText("")
        self.bt_Home.setFlat(True)
        self.bt_Home.setObjectName("bt_Home")

        # botao ajuda
        self.bt_Ajuda = QtWidgets.QPushButton(self.wd_topo)
        self.bt_Ajuda.setGeometry(QtCore.QRect(900, 5, 50, 50))
        self.bt_Ajuda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Ajuda.setStyleSheet(styleSuperior)
        self.bt_Ajuda.setText("")
        self.bt_Ajuda.setFlat(True)
        self.bt_Ajuda.setObjectName("bt_Ajuda")

        # botao saida
        self.bt_Exit=QtWidgets.QPushButton(self.wd_topo)
        self.bt_Exit.setGeometry(QtCore.QRect(950, 5, 50, 50))
        self.bt_Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Exit.setWhatsThis("")
        self.bt_Exit.setStyleSheet(styleSuperior)
        self.bt_Exit.setText("")
        self.bt_Exit.setFlat(True)
        self.bt_Exit.setObjectName("bt_Exit")
        self.bt_Exit.clicked.connect(MainWindow.close)

        """ Final Menu Topo"""
        """ Comeco Menu """

        # widget menu janelas
        self.wd_menu=QtWidgets.QWidget(self.centralwidget)
        self.wd_menu.setGeometry(QtCore.QRect(0, 60, 1000, 40))
        self.wd_menu.setStyleSheet("background: rgb(57, 151, 54);")
        self.wd_menu.setObjectName("wd_menu")

        styleLbTitulo = "QLabel{\n" \
            "font-size: 20px;\n" \
            "font-family: \"Arial\";\n" \
            "font-weight: bold;\n" \
            "color: #FFF;\n" \
            "}"

        # label do caminho atual
        self.lb_Caminho = QtWidgets.QLabel(self.centralwidget)
        self.lb_Caminho.setGeometry(QtCore.QRect(10, 70, 1000, 20))
        self.lb_Caminho.setFont(font)
        self.lb_Caminho.setStyleSheet(styleLbTitulo)
        self.lb_Caminho.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_Caminho.setObjectName("lb_Caminho")

        """ Final Menu"""

        # frame com conteudo pagina
        self.ct_conteudo=QtWidgets.QFrame(self.centralwidget)
        self.ct_conteudo.setGeometry(QtCore.QRect(0, 100, 1000, 600))
        self.ct_conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ct_conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ct_conteudo.setObjectName("ct_conteudo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.translateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def translateUi(self, MainWindow):
        _translate=QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Sistema de Floricultura"))
        self.bt_HomeLogo.setToolTip(_translate("MainWindow", "Tela Inicial Logo"))
        self.lb_BemVindo.setText(_translate("MainWindow", "Bem Vindo ao"))
        self.lb_BemVindo2.setText(_translate("MainWindow", "Classificador de Pneumonia"))
        self.bt_Home.setToolTip(_translate("MainWindow", "Tela Inicial"))
        self.bt_Ajuda.setToolTip(_translate("MainWindow", "Ajuda"))
        self.bt_Exit.setToolTip(_translate("MainWindow", "Sair"))
        self.lb_Caminho.setText(QtWidgets.QApplication.translate("lb_Caminho", "Home", None, -1))
