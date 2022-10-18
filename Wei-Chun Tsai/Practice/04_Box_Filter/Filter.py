import cv2
import os
import matplotlib.pyplot as plt

DIR = 'images/'

class ColorModel:

    def __init__(self):
        pass

    def rgb2gray(file):
        file = os.path.join(DIR, file)
        rgb_img = cv2.imread(file)
        gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('misc/IMG_Gray_Filter.jpg', gray_img)
        return gray_img

class Filter:

    def __init__(self):
        pass

    def box(image):

        box_blur_img = cv2.blur(image, (5, 5))
        plt.subplot(1, 2, 1)
        plt.title('Original Image')
        plt.imshow(image, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.title('Box Filter')
        plt.imshow(box_blur_img, cmap='gray')

        plt.savefig('misc/Box Filter Effect.png')

        plt.show()
