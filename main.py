import cv2
import numpy as np
from matplotlib import pyplot as plt

files = ['Semaforo_verd_1.jpg', 'Semaforo_verd_2.jpg', 'Semaforo_verd_2.jpg',
         'Semaforo_verd_3.jpg', 'Semaforo_verd_4.jpg', 'Semaforo_verd_5.jpg',
         'Semaforo_verd_5.jpg', 'Semaforo_verd_5.jpg', 'Semaforo_verd_6.jpg',
         'Semaforo_verm_1.jpg', 'Semaforo_verm_2.jpg', 'Semaforo_verm_3.jpg',
         'Semaforo_verm_4.jpg', 'Semaforo_verm_4.jpg', 'Semaforo_verm_5.jpg',
         'Semaforo_verm_5.jpg', 'Semaforo_verm_5.jpg', 'Semaforo_verm_6.jpg']

box = [[(57, 43), (85, 125)],
       [(65, 40), (95, 133)],
       [(205, 40), (233, 133)],
       [(58, 35), (96, 150)],
       [(189, 18), (212, 76)],
       [(77, 47), (105, 133)],
       [(137, 47), (165, 133)],
       [(195, 47), (222, 133)],
       [(39, 20), (72, 129)],
       [(110, 80), (150, 222)],
       [(128, 20), (168, 138)],
       [(75, 33), (110, 155)],
       [(42, 25), (63, 100)],
       [(195, 25), (215, 100)],
       [(180, 25), (206, 136)],
       [(130, 60), (156, 150)],
       [(83, 105), (106, 169)],
       [(120, 25), (150, 134)]]

for i in range(18):
    img = cv2.imread(files[i], 1)
    mask = img[box[i][0][1]:box[i][1][1], box[i][0][0]:box[i][1][0]]
    cv2.imshow('Mascara', mask)
    cv2.imwrite('cortada.jpg', mask)

    b, g, r = cv2.split(mask)

    plt.title('Histograma')
    hst_azul = plt.hist(b.ravel(), 32, [0, 256])
    hst_verde = plt.hist(g.ravel(), 32, [0, 256])
    hst_vermelho = plt.hist(r.ravel(), 32, [0, 256])
    plt.show()

    azul = np.sum(hst_azul[0][0:32])
    verde = np.sum(hst_verde[0][0:32])
    vermelho = np.sum(hst_vermelho[0][0:32])

    print('azul:{}'.format(azul))
    print('verde:{}'.format(verde))
    print('vermelho:{}'.format(vermelho))

    if 115 < vermelho < 1000 and azul < 300 and verde < 198:
        print('Vermelho')

    if verde > 200 and vermelho > 300 and azul < 150:
        print('Amarelo')
    else:

        if verde > 110:
            print('Verde')

    img = cv2.rectangle(img, box[i][0], box[i][1], (255, 0, 0), 2)
    cv2.imshow('Original', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
