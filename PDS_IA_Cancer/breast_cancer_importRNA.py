#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:07:50 2020

@author: ricardovargas
"""

'''
 Start Carregando RNA salva
'''

import numpy as np
from keras.models import model_from_json

arquivo = open('classificador_breast.json', 'r')
estrutura_rede = arquivo.read()
arquivo.close()

classificador = model_from_json(estrutura_rede)

'''
 End Carregando RNA salva
 Start Carregando Pesos RNA
'''

classificador.load_weights('classificador_breast.hb5')

'''
 End Carregando Pesos RNA
 Start Carregando Exemplo Entrada
'''

novo = np.array([[15.88, 8.34, 118, 900, 0.10, 0.08, 0.134, 0.178, 0.20, 0.05,
                  1098, 0.97, 4500, 145.2, 0.005, 0.04, 0.05, 0.015, 0.03,
                  0.007, 23.15, 16.64, 178.5, 2018, 0.14, 0.185, 0.84, 158,
                  0.363]])

'''
 End Carregando Exemplo Entrada
 Start Classificacao
'''

previsao = classificador.predict(novo)
previsao = (previsao > 0.8)

'''
 End Classificacao
'''
