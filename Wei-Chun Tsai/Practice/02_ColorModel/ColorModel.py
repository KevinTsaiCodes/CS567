import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

DIR = 'images/'

class Transformation:

    def __init__(self):
        pass

    def rgb2gray(file):
        file = os.path.join(DIR, file)
        rgb_img = cv2.imread(file)
        gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('misc/IMG_Gray.jpg', gray_img)

        plt.subplot(1, 2, 1)
        plt.imshow(rgb_img, cmap='gray')
        plt.title('Original Image')
        plt.xticks([])
        plt.yticks([])

        plt.subplot(1, 2, 2)
        plt.imshow(gray_img, cmap='gray')
        plt.title('Gray-Scale Image')
        plt.xticks([])
        plt.yticks([])

        plt.savefig('misc/IMG_RGB_Gray.pdf')
        plt.show()

        return gray_img
