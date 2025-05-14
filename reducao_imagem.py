import cv2
import matplotlib.pyplot as plt

# Caminho completo para a imagem
caminho_imagem = '/Users/hey/Documents/Cursos/Machine Learning com a Baireesdev/pythonProject/lena.png'

# Carrega a imagem colorida
imagem_colorida = cv2.imread(caminho_imagem)

# Verifica se a imagem foi carregada com sucesso
if imagem_colorida is None:
    print("Erro: imagem não encontrada. Verifique o caminho.")
    exit()

# Converte de BGR para RGB
imagem_rgb = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)

# Converte para tons de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Binarização (threshold)
_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Exibição
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Colorida")
plt.imshow(imagem_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Cinza")
plt.imshow(imagem_cinza, cmap='gray')
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Binarizada")
plt.imshow(imagem_binarizada, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()
