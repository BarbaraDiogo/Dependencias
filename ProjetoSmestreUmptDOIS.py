import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow # para exibir imagens dentro do COLAB
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt

from google.colab import files
uplaoded = files.upload()

print ('='*100)
print ('Ler e exibir uma imagem em BGR')
print ('='*100)

imgBGR = cv.imread('tobi.jpg')
cv2_imshow(imgBGR)

print ('='*100)
print ('Converter uma imagem BGR em RGB e exibi-la em RGB - ERRADO')
print ('='*100)

imgRGB = cv.cvtColor(imgBGR, cv.COLOR_BGR2RGB)
cv2_imshow(imgRGB)

print ('='*100)
print ('Converter uma imagem que está em RGB para GRAY e fazer sua exibição nesse formato convertido')
print ('='*100)

imgGRAY = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)
cv2_imshow(imgGRAY)


#Fazendo o histograma:
print ('='*45)
print ('Exibir o histograma da imagem CINZA (GRAY)')
print ('='*45)

plt.hist(imgGRAY.ravel(), bins=256, range=[0,255])
plt.show()

#Usando a função para escolhero melhor threshold e covertendo a imagem CINZA para BINÁRIA:
(thresh, BW_otsu) = cv.threshold(imgGRAY, thresh, 255, cv.THRESH_OTSU)
print ('='*100) 
print(f'Covertendo a imagem CINZA para BINÁRIA e o valor de threshold retornado o método de Otsu foi: {thresh}')
print ('='*100)
cv2_imshow(BW_otsu)


from google.colab import files
uplaoded = files.upload()

imagemBGR = cv.imread('niveis_cinza.png')

print ('='*15)
print ('Exibir a imagem') #Fazer upload, ler e exibir a imagem niveis_cinza (1, 2 e 3)
print ('='*15)

imagemRGB = cv.cvtColor(imagemBGR, cv.COLOR_BGR2RGB)
cv2_imshow(imagemRGB)

print ('='*40)
print ('Exibir o histograma com os thresholdings') # Exibir o histograma e possiveis threshshold (4)
print ('='*40)

plt.hist(imagemRGB.ravel(), bins=256, range=[0,255])
plt.show()

(thresh, BW) = cv.threshold(imagemRGB, 0, 255, cv.THRESH_BINARY) 
print ('='*80)
print ('Gerar e exibir uma imagem binária que apareça apenas o PRIMEIRO retângulo') #Exercicio 5 do desafio
print ('='*80)
cv2_imshow(BW)

(thresh, BW) = cv.threshold(imagemRGB, 64, 255, cv.THRESH_BINARY)
print ('='*100)
print ('Gerar e exibir uma imagem binária que apareça apenas o PRIMEIRO e o SEGUNDO retângulo')#Exercicio 6 do desafio
print ('='*100)
cv2_imshow(BW)

(thresh, BW) = cv.threshold(imagemRGB, 128, 255, cv.THRESH_BINARY)
print ('='*100)
print ('Gerar e exibir uma imagem binária que apareça apenas o PRIMEIRO, o SEGUNDO e o TERCEIRO retângulo')#Exercicio 7 do desafio
print ('='*100)
cv2_imshow(BW)

(thresh, BW) = cv.threshold(imagemRGB, 192, 255, cv.THRESH_BINARY)
print ('='*75)
print ('Gerar e exibir uma imagem binária que apareça TODOS os retângulo')#Exercicio 8 do desafio
print ('='*75)
cv2_imshow(BW)

print ('='*30)
print ('Exibir a imagem original')
print ('='*30)
cv2_imshow(imgBGR)
#/////////////////////////////////////////
print('='*50)
print ('Clarear a imagem original')
print ('='*50)
imgBGR_clara = (100.0/255)*imgBGR + 100
cv2_imshow(imgBGR_clara)
#/////////////////////////////////////////
print ('='*50)
print ('Escurecer a imagem original')
print ('='*50)
imgBGR_escurecida = 255.0*(imgBGR/255.0)**4
cv2_imshow(imgBGR_escurecida)
#/////////////////////////////////////////
print ('='*55)
print ('Deixar a imagem original negativa')
print ('='*55)
imgBGR_negativa = 255 - imgBGR
cv2_imshow(imgBGR_negativa)
