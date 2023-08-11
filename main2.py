import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Semaforo_verd_1.jpg', 0)

mask_verde = img[100:125, 57:85]
mask_amarelo = img[70:95, 57:85]
mask_vermelho = img[40:65, 57:85]

cv2.imshow('ola', mask_vermelho)

plt.title('Vermelho')
hst_red = plt.hist(mask_vermelho.ravel(), 16, [0, 256])
plt.show()
plt.title('Verde')
hst_verde = plt.hist(mask_verde.ravel(), 16, [0, 256])
plt.show()
plt.title('Amarelo')
hst_amarelo = plt.hist(mask_amarelo.ravel(), 16, [0, 256])
plt.show()

verde = np.sum(hst_verde[0][10:16])
amarelo = np.sum(hst_amarelo[0][10:16])
vermelho = np.sum(hst_red[0][10:16])


print(f'Valor vermelho: {vermelho}')
print(f'Valor amarelo: {amarelo}')
print(f'Valor verde: {verde}')

if vermelho > 130:
    print("Vermelho Ligado")
if amarelo > 130:
    print("Amarelo Ligado")
if verde > 130:
    print("Verde ligado")

cv2.waitKey(0)
cv2.destroyAllWindows()