import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

DIR = 'images/'

class EdgeDetection:

    def __init__(self):
        pass

    def laplacian(image):
        lap_image = cv2.Laplacian(image, None, ksize = 5)
        lap_image = cv2.convertScaleAbs(lap_image)

        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Original in Grayscale')

        plt.subplot(1, 2, 2)
        plt.imshow(lap_image, cmap='gray')
        plt.title('Laplacian in Grayscale')

        plt.show()
