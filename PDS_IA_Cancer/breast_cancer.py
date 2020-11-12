#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:52:43 2020

@author: ricardovargas
"""

'''
 Start Processando Dados
'''

import pandas as pd

# base de dados para usar na previsao
previsores = pd.read_csv('entradas_breast.csv')
# base de dados das respostas do cancer (saida == classe)
classe = pd.read_csv('saidas_breast.csv')

from sklearn.model_selection import train_test_split
# divide os dados pro processamento conforme porcentagem pedida
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25)

'''
 End Processando Dados
 Start Criar estrutura RNA
'''

import keras

#modelo de classe pra criar a RNA
from keras.models import Sequential

#rede de camadas densa fullyconnected
from keras.layers import Dense

#criando modelo de RNA
classificador = Sequential()

'''
 End Criar estrutura RNA
 Start Configurar RNA
'''

#criando camada oculta de 16
# units=16 devido (camadas de entrada + camada de saida)/2 ou seja (30+1)/2=15.5
# input_dim=30 ja que existem 30 atributos nas entradas (30 colunas de variaveis)
# uma saida por causa de classificacao 1 ou 0
classificador.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform', input_dim=30))

# segunda camada oculta
classificador.add(Dense(units=16, activation='relu', kernel_initializer='random_uniform'))

# camada de saida com 1 saida
classificador.add(Dense(units=1, activation='sigmoid'))

#criando metodo de otimizacao com Adam lr=learning rate
otimizador = keras.optimizers.Adam(lr=0.001, decay=0.0001, clipvalue=0.5)

# configura metodo de otimizacao danRNA
classificador.compile(optimizer=otimizador, loss='binary_crossentropy', metrics=['binary_accuracy'])

'''
 End Configurar RNA
 Start Treinamento RNA
'''

#classificador.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

# realizando treinamento
classificador.fit(previsores_treinamento, classe_treinamento, batch_size=10, epochs=100)

'''
 End Treinamento RNA
 Start Pesos RNA
'''

#pesos apos o treinamento
peso0 = classificador.layers[0].get_weights()
print(peso0)
print(len(peso0))

#primeira camada oculta
peso1 = classificador.layers[1].get_weights()

#segunda camada oculta
peso2 = classificador.layers[2].get_weights()

'''
 End Pesos RNA
 Start Execucao Teste Predicao RNA
'''

# teste usando a base de teste (25%)
previsoes = classificador.predict(previsores_teste)

# configura a saida
previsoes = (previsoes > 0.5)

'''
 End Execucao Teste Predicao RNA
 Start Evaluacao Teste RNA
'''

# mede o acerto
from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)

# cria matriz de confusao para realizar avaliacao
matriz = confusion_matrix(classe_teste, previsoes)

'''
 End Evaluacao Teste RNA
 Start Previsao RNA
'''

#faz previsao usando o keras
resultado = classificador.evaluate(previsores_teste, classe_teste)

'''
 End Previsao RNA
 Start Salvando e Pesos RNA
'''

#obtendo estrutura RNA
classificador_json = classificador.to_json()

# salvando em arquivo
with open('classificador_breast.json', 'w') as json_file:
    json_file.write(classificador_json)

# salvando pesos em disco
classificador.save_weights('classificador_breast.h5')

'''
 End Salvando e Pesos RNA
'''
