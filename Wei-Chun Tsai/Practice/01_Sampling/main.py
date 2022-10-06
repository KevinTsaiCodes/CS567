import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

DIR = 'images/'

if __name__ == '__main__':
    name = 'lena.png'
    file = cv2.imread(os.path.join(DIR, name))
    file = cv2.cvtColor(file, cv2.COLOR_BGR2RGB)
    file = cv2.cvtColor(file, cv2.COLOR_RGB2GRAY)
    gray_2 = file[0 : -1 : 256, 0 : -1 : 256]
    gray_4 = file[0 : -1 : 64, 0 : -1 : 64]
    gray_8 = file[0 : -1 : 32, 0 : -1 : 32]
    gray_16 = file[0 : -1 : 16, 0 : -1 : 16]
    gray_32 = file[0 : -1 : 8, 0 : -1 : 8]
    plt.subplot(2, 3, 1)
    plt.imshow(gray_2, cmap='gray')
    plt.subplot(2, 3, 2)
    plt.imshow(gray_4, cmap='gray')
    plt.subplot(2, 3, 3)
    plt.imshow(gray_8, cmap='gray')
    plt.subplot(2, 3, 4)
    plt.imshow(gray_16, cmap='gray')
    plt.subplot(2, 3, 5)
    plt.imshow(gray_32, cmap='gray')
    plt.subplot(2, 3, 6)
    plt.imshow(file, cmap='gray')
    plt.savefig('Sampling Lena.jpg')
    plt.show()
