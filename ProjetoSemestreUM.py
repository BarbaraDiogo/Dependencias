import numpy as np
import pandas as pd
import cv2 as cv 
from google.colab.patches import cv2_imshow # para exibir imagens dentro do COLAB
from skimage import io
from PIL import Image 
import matplotlib.pylab as plt

urls = ["https://iiif.lib.ncsu.edu/iiif/ua016_035-guiarduet_DRB/square/300,/0/default.jpg", 
"https://iiif.lib.ncsu.edu/iiif/technician-The-Last-Page-2003-05-01_0001/!square/300,/0/default.jpg",
"https://iiif.lib.ncsu.edu/iiif/0052711/square/300,/0/default.jpg"]
for url in urls:
  imagesBGR = io.imread(url)
  imagesRGB = cv.cvtColor(imagesBGR, cv.COLOR_BGR2RGB)
  final_frame = cv.hconcat((imagesBGR, imagesRGB))
  cv2_imshow(final_frame)
  print('\n')

# 1) abrir e exibir uma nova imagem de sua escolha (Não se esqueça das convesões)
print('=' * 100)
print('1)Para carregar e exibir a imagem')
print('=' * 100)
url = "https://placekitten.com/200/300"
imagemBGR = io.imread(url)
imagemRGB = cv.cvtColor(imagemBGR, cv.COLOR_BGR2RGB)
cv2_imshow(imagemRGB)
print('\n')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2) exibir a largura da imagem
print('=' * 100)
print('2)Exibir a largura da imagem')
print('=' * 100)
w = imagemRGB.shape[1]
print('\n')
print('A larura da imagem é: ', w)
print('\n')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3) exibir a matriz de VERDE
print('=' * 100)
print('3)Acessando a matriz verde')
print('=' * 100)
G = imagemRGB[:,:,1]
print('\n')
print(G)
print('\n')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 4) exibir as 3 cores do último pixel
print('=' * 100)
print('4)Exibindo as 3 ultimas cores do ultimo pixel')
print('=' * 100)
h = imagemRGB.shape[0] #como a largura já sabemos no 2), calculei somente a altura
print('\n')
w = w - 1 #a matriz começa de 0 e vai até 2 (coluna e linha), portanto são 3 valores nessas 3 posições, e para sabermos o da ultima posição precisamos subtrair 1
h = h - 1 #pela matriz começar em [0,0] temos que fazer essa subtração de 1
print('\n')
R = imagemRGB[:,:,0] #lembrando que a matriz verde já descobrimos em 3)
B = imagemRGB[:,:,2]
print('\n')
print("Ultimo pixel da matriz vermelha: ", R[h, w]) #sendo width = linha e height = coluna ---> 1°coluna e 2°linha [1,1]
print('\n')
print("Ultimo pixel da matriz verde: ", G[h, w])
print('\n')
print("Ultimo pixel da matriz azul: ", B[h, w])
print('\n')

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 5) exibir os valores de AZUL para a LINHA central da imagem, ou seja, encontre a metade da ALTURA da imagem para imprimir todas as COLUNAS
print('=' * 100)
print('5)Acessando os valores de AZUL para a LINHA central da imagem')
print('=' * 100)
print('\n')
met_col = int(h/2) #descobrindo o valor da metade da altura e precisa ser um numero inteiro (int())
print('Os valores de azul para a linha central sao: \n', B[met_col,0:w])
print('\n')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 6) exibir os valores de VERMELHO para a COLUNA central da imagem, ou seja, encontre a metade da LARGURA da imagem para imprimir todas as LINHAS
print('=' * 100)
print('6)Acessando os valores de VERMELHO para a COLUNA central da imagem')
print('=' * 100)
print('\n')
met_w = int(w/2) #descobrindo o valor da metade da largura e precisa ser um numero inteiro (int())
print('Os valores de vermelho para a coluna central sao: \n', R[0:h,met_w])
print('\n')


# 1) abrir e exibir uma nova imagem de sua escolha (diferente das anteriores)
print('='*100)
print('1)Carregar e exibir a primeira imagem')
print('='*100)
urls = "https://lojamagma.vteximg.com.br/arquivos/ids/159940-650-650/pvc-mini-queops-arcoires.jpg?v=637038272404300000"
imagemBGR = io.imread(urls)  
imagemRGB = cv.cvtColor(imagemBGR, cv.COLOR_BGR2RGB)
cv2_imshow(imagemRGB)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2) calcular e exibir o histograma dos 3 canais no mesmo gráfico
print('='*100)
print('2)Histograma dos 3 canais em um mesmo grafico (1° imagem)')
print('='*100)

color = ('r','g','b')
for i,col in enumerate(color):
    hist = cv.calcHist([imagemRGB],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3) Repita os passos 1 e 2 para mais outra imagem de sua escolha
print('='*100)
print('3.1)Carregar e exibir a segunda imagem')
print('='*100)
url = "https://static.preparaenem.com/conteudo_legenda/ac2c7481814c05b81f6f305b8a134b86.jpg"
iBGR = io.imread(url)  
iRGB = cv.cvtColor(iBGR, cv.COLOR_BGR2RGB)
cv2_imshow(iRGB)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print('='*100)
print('3.1.1)Histograma dos 3 canais em um mesmo grafico (2° imagem)')
print('='*100)

color = ('r','g','b')
for i,col in enumerate(color):
    hist = cv.calcHist([iRGB],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print('='*100)
print('3.2)Carregar e exibir a terceira imagem')
print('='*100)
url = "https://i.pinimg.com/originals/76/f3/fe/76f3feac5a6a34a38ee21f012f7be6c1.jpg"
imBGR = io.imread(url)  
imRGB = cv.cvtColor(imBGR, cv.COLOR_BGR2RGB)
cv2_imshow(imRGB)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print('='*100)
print('3.2.1)Histograma dos 3 canais em um mesmo grafico (3° imagem)')
print('='*100)

color = ('r','g','b')
for i,col in enumerate(color):
    hist = cv.calcHist([imRGB],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()