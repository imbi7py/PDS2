# coding=utf-8
import sys
import os
import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Conexao(object):
    def __init__(self, database='floricultura'):
        self.DbHost = "127.0.0.01"
        self.DbName = database
        self.DbUser = "root"
        self.DbPassword = "zpesystems"
        self.engine = ""
        self.Base = ""
        self.Session = ""

        # Caminho absoluto config.ini
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        config = configparser.ConfigParser()
        config.sections()

        # Engine
        self.engine = create_engine(
            'mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8'
            .format(self.DbUser, self.DbPassword,
                    self.DbHost, self.DbName),
            echo=False)
        # Criando Sessao
        self.Session = sessionmaker(bind=self.engine)

Base = declarative_base()
