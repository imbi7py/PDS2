# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui',
# licensing of 'home.ui' applies.
#
# Created: Mon Mar 18 01:06:11 2019
#      by: PyQt5-uic  running on PyQt5 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_ct_Home(object):
    def setHome(self, ct_Home):
        styleBlock = "QFrame {\n" \
        "background: #FFF;\n" \
        "border: none;\n" \
        "border-radius: 20px\n" \
        "}"

        styleLbTitulo = "QLabel{\n" \
        "font-size: 20px;\n" \
        "font-family: \"Arial\";\n" \
        "font-weight: bold;\n" \
        "color: #A2A2A2;\n" \
        "}"

        styleBtInicio= "QPushButton{\n" \
            "background-color: #7AB32E;\n" \
            "border-radius: 2px;\n" \
            "padding: 2px;\n" \
            "color: #FFF;\n" \
            "font: 10px \"Tahoma\" Bold\n" \
            "}\n" \
            "QPushButton:hover{\n" \
            "background-color: #40a286\n" \
            "}"

        ct_Home.setObjectName("ct_Home")
        ct_Home.resize(1000, 600)
        ct_Home.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HomeFrame = QtWidgets.QFrame(ct_Home)
        self.HomeFrame.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.HomeFrame.setObjectName("HomeFrame")

        self.fr_Home = QtWidgets.QFrame(self.HomeFrame)
        self.fr_Home.setGeometry(QtCore.QRect(100, 50, 800, 500))
        self.fr_Home.setStyleSheet(styleBlock)
        self.fr_Home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_Home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_Home.setObjectName("fr_VendasAbertas")

        self.bt_Flor = QtWidgets.QPushButton(self.fr_Home)
        self.bt_Flor.setGeometry(QtCore.QRect(150, 20, 500, 300))
        self.bt_Flor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Flor.setStyleSheet(styleLbTitulo)
        self.bt_Flor.setText("")
        self.bt_Flor.setFlat(True)
        self.bt_Flor.setObjectName("bt_Flor")

        self.lb_TituloHome = QtWidgets.QLabel(self.fr_Home)
        self.lb_TituloHome.setGeometry(QtCore.QRect(150, 320, 500, 20))
        self.lb_TituloHome.setStyleSheet(styleLbTitulo)
        self.lb_TituloHome.setObjectName("lb_TituloHome")

        self.bt_Iniciar = QtWidgets.QPushButton(self.fr_Home)
        self.bt_Iniciar.setGeometry(QtCore.QRect(350, 350, 100, 40))
        self.bt_Iniciar.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.bt_Iniciar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Iniciar.setStyleSheet(styleBtInicio)
        self.bt_Iniciar.setText("")
        self.bt_Iniciar.setFlat(True)
        self.bt_Iniciar.setObjectName("bt_Iniciar")

        self.translateUiHome(ct_Home)
        QtCore.QMetaObject.connectSlotsByName(ct_Home)

    def translateUiHome(self, ct_Home):
        ct_Home.setWindowTitle(QtWidgets.QApplication.translate("ct_Home", "Frame", None, -1))
        self.lb_TituloHome.setText(QtWidgets.QApplication.translate("lb_TituloHome", "Sistema de Classificação para Casos de Pneumonia", None, -1))
        self.bt_Iniciar.setText(QtWidgets.QApplication.translate(
            "bt_Iniciar", "Iniciar", None, -1))
    

