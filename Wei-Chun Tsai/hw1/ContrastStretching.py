import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

DIR = 'images/'

class ColorModel:

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


class ContrastStretching:

    def __init__(self):
        pass

    def normalize(gray_img):
        gray_intensity = gray_img
        InP = gray_intensity  # Input pixel value
        minI = 10  # 可操控值, TODO, minimum pixel value in the input image
        maxI = 100  # 可操控值, TODO, minimum pixel value in the input image
        minO = np.min(gray_intensity)  # Minimum pixel value in the output image
        maxO = np.max(gray_intensity) # Maximum pixel value in the output image
        OutP = (InP - minI) * ( ( (maxO - minO) / (maxI - minI) ) + minO)  # Output pixel value
        cv2.imwrite('misc/High-Contrast.jpg', OutP)
        return OutP
    
class VersusImage:

    def __init__(self):
        pass

    def plot_image(gray_img, output_img):
        plt.subplot(1, 2, 1)
        plt.imshow(gray_img, cmap='gray')
        plt.title('Gray Scale')
        plt.xticks([])
        plt.yticks([])

        plt.subplot(1, 2, 2)
        plt.imshow(output_img, cmap='gray')
        plt.title('Contrast Stretching')
        plt.xticks([])
        plt.yticks([])
        plt.show()
