# Importa as bibliotecas necessárias
import matplotlib.pyplot as plt
from PIL import Image

# Lê a imagem colorida e a armazena em uma matriz
image_file = Image.open("/Users/vituu/Python/image_py.png")

# Gera a imagem colorida na memória do computador
imgplot = plt.imshow(image_file)
plt.show()  # Imprime na tela a imagem colorida

# Converte a imagem para tons de cinza
image_file = image_file.convert('L')

# Gera a imagem em tons de cinza na memória do computador
imgplot = plt.imshow(image_file)
plt.show()  # Imprime na tela a imagem em tons de cinza