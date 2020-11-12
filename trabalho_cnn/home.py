# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt

from Views.home import Ui_ct_Home

class MainHome(Ui_ct_Home):

    def main_home(self, frame):
        super(MainHome, self).setHome(frame)
        self.HomeFrame.show()
        self.IconeFlorHome(self.bt_Flor, self.resourcepath('Images/janelahome.jpg'))
        self.bt_Iniciar.clicked.connect(self.checkConfiguration)
