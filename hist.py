import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Semaforo_verd_1.jpg', 1)

blue_hist = cv.calcHist([img], [0], None, [256], [0, 256])
green_hist = cv.calcHist([img], [1], None, [256], [0, 256])
red_hist = cv.calcHist([img], [2], None, [256], [0, 256])

cv.imshow('ola', blue_hist)
cv.waitKey(3000)
cv.destroyAllWindows()
'''
for i, col in enumerate(['b', 'g', 'r']):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.show()