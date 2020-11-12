# -*- coding: utf-8 -*-
import sys
import os
import configparser

class Conexao(object):
    def __init__(self, pathRNA="", pathPesos=""):
        self.pathRNA = pathRNA
        self.pathPesos = pathPesos
        self.pathConfig = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "config.ini")
        self.estrutura_rede = ""
        self.classificador = ""

        config = configparser.ConfigParser()
        config.sections()
        if config.read(self.pathConfig):
            self.pathRNA = config['DEFAULT']['pathRNA']
            self.pathPesos = config['DEFAULT']['pathPesos']
        else:
            self.pathRNA = ""
            self.pathPesos = ""

    def isConfigurada(self):
        if (self.pathRNA == "" or self.pathPesos == ""):
            return False
        else:
            return True

    def salvar(self):
        if(self.isConfigurada()):
            config = configparser.ConfigParser()
            config['DEFAULT'] = { 'pathRNA': self.pathRNA, 'pathPesos': self.pathPesos}
            with open(self.pathConfig, 'w') as configfile:
                config.write(configfile)