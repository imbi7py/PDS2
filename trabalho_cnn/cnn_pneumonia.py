   #importação das bibliotecas a serem utilizadas
#inclusive para realizar as etapas de convolução 
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from sklearn.metrics import classification_report, confusion_matrix

import numpy as np
import os
import matplotlib.pyplot as plt #for plotting things

from keras.models import model_from_json
from keras.preprocessing import image

"""
    1,2,3,4 - prepara os dados
"""

#ImageDataGenerator padroniza a estutura de dados das imagens
#i.e: o atributo de rescale normaliza as imagens com valores de pixels 1 à 255
gerador_treinamento = ImageDataGenerator(rescale = 1./255,
                                         rotation_range=7,
                                         horizontal_flip=True,
                                         shear_range=0.2,
                                         height_shift_range= 0.07,
                                         zoom_range=0.2)
gerador_teste = ImageDataGenerator(rescale = 1./255)

# 1 - carregar os dados de treinamento
#carregar os dados para treinamento
base_treinamento = gerador_treinamento.flow_from_directory('chest_xray/chest_xray/train',
                                                           target_size= (64,64),
                                                           batch_size=32, 
                                                           class_mode ='binary')

#carregar os dados para teste
base_teste = gerador_teste.flow_from_directory('chest_xray/chest_xray/test',
                                               target_size= (64,64),
                                               batch_size=32,
                                               class_mode='binary')
#carregar os dados para validar no fim
base_validacao = gerador_teste.flow_from_directory('chest_xray/chest_xray/val',
                                                   target_size=(64, 64),
                                                   batch_size=32,
                                                   class_mode='binary')

"""
    5 - define a rede neural
"""

#definindo a RNA
classificador = Sequential()
# criando a 1 camada de convolução
#filters              - 32 é os pixels
#kernel_size          - matriz 3x3 para fazer a multiplicação da matriz (imagem original x kernel)
#input_shape arg 1, 2 - imagens 64 x 64 para padronizar
#input_shape arg 3    - 3 canais para informar que é rgb
#activation           - relu retira parte mais escuras (valores negativos)
classificador.add(Conv2D(32, (3,3), input_shape = (64, 64, 3), activation='relu'))
#pega o mapa de característica e normaliza os valores entre 0 e 1
classificador.add(BatchNormalization())
#matriz do max pooling com as principais características matrix 2x2
classificador.add(MaxPooling2D(pool_size=(2,2)))

# criando a 2 camada de convolução
#filters              - 32 pixels
#kernel_size          - matriz 3x3 para fazer a multiplicação da matriz (imagem original x kernel)
#input_shape arg 1, 2 - imagens 64 x 64 para padronizar
#input_shape arg 3    - 3 canais para informar que é rgb
#activation           - relu retira parte mais escuras (valores negativos)
classificador.add(Conv2D(32, (3,3), input_shape = (64, 64, 3), activation='relu'))
classificador.add(BatchNormalization())
classificador.add(MaxPooling2D(pool_size=(2,2)))

#ultima etapa da convolução
#alterando a estrutura de dados de matriz para vetor atráves do flattering
classificador.add(Flatten())

#criando 1 camada oculta com 128 neuronios = 64+64 características 
#cada imagem tem 64x64 pixels de dimensao cada pixel uma característica
classificador.add(Dense(units = 128, activation='relu'))
#o dropout para zerar algumas entradas da camada oculta, neste caso 20%
classificador.add(Dropout(0.2))

#criando 2 camada oculta 
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dropout(0.2))

#criando a camada de saída da RNA
# sigmoid vai descendo o ponto gradualmente
classificador.add(Dense(units=1, activation='sigmoid'))

#configurando atributos para o treinamento
classificador.compile(optimizer='adam', loss = 'binary_crossentropy', 
                      metrics = ['accuracy'])

classificador.summary()

"""
    6 - faz treinamento
"""

# faz o treinamento
#steps_per_epoch=5216 é a qtd de imagens da base de treinamento
#validation_steps=624 é a qtd de imagens da base de teste
#epochs=10 interfere na qualidade do treinamento
#modelo_classificador = classificador.fit_generator(base_treinamento, steps_per_epoch=5216/32,
#                            epochs=5, validation_data=base_validacao, 
#                            validation_steps=624/32)

modelo_classificador = classificador.fit_generator(base_treinamento, steps_per_epoch=5216/32,
                            epochs=10, validation_data=base_validacao, 
                            validation_steps=624/32)

"""
    9,10 - salva pesos e RNA
"""

#salvando os pesos em disco
classificador.save_weights('pesos_pneumonia.h5')

#obtendo a estrutura da RNA
classificador_json = classificador.to_json()
#gravando em disco
with open('cnn_pneumonia.json', 'w') as json_file:
    json_file.write(classificador_json)

"""
    6 - dados de precisao
"""

test_accurancy = classificador.evaluate_generator(base_teste, steps=624)
print('A acuracia do teste é:', test_accurancy[1]*100, '%')

predicoes = classificador.predict_generator(base_teste, 100)
print('Predicoes: ', predicoes)
predicoes = (predicoes > 0.5)
print('Predicoes: ', predicoes)

# Accuracy 
plt.plot(modelo_classificador.history['accuracy'])
plt.plot(modelo_classificador.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training set', 'Validation set'], loc='upper left')
plt.show()

# Loss 
plt.plot(modelo_classificador.history['val_loss'])
plt.plot(modelo_classificador.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training set', 'Test set'], loc='upper left')
plt.show()


""" TESTING IMAGE """

path_imagem = "chest_xray/chest_xray/val/PNEUMONIA/person1947_bacteria_4876.jpeg"
path_imagem = "chest_xray/chest_xray/val/NORMAL/NORMAL2-IM-1436-0001.jpeg"
arquivo = open('cnn_pneumonia.json', 'r')
estrutura_rede = arquivo.read()
arquivo.close()

classificador = model_from_json(estrutura_rede)
classificador.load_weights('pesos_pneumonia.h5')

imagem_teste = image.load_img(path_imagem, target_size = (64,64))
            
#alterar o formato da imagem de teste
imagem_teste = image.img_to_array(imagem_teste)

#ver os valores de cada pixel de image_teste
#normalizando esses valores na escala de 0 - 1
imagem_teste /= 255

#alterando o formato para o tensor flow adicionando mais uma coluna
imagem_teste = np.expand_dims(imagem_teste, axis = 0)

#realizado essas configurações já podemos realizar a previsão
previsao = classificador.predict(imagem_teste)
print("predicao em pontos: ", previsao)
#retornando false para normal e verdadeiro para pneumonia
previsao = (previsao > 0.5)
print("predicao em boolean: ", previsao)
if(previsao[0] == True):
  print("Resultado: Pneumonia")
else:
  print("Resultado: Caso Normal")


