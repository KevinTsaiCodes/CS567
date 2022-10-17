import cv2
import numpy as np

class Filter:

    def __init__(self):
        pass

    def Median(high_contrast_img):
        result_img = cv2.medianBlur(np.uint8(high_contrast_img), 5)
        return result_img

    def Mean(high_contrast_img):
        

    def Bilateral(high_contrast_img):
        pass

    def Gaussian(high_contrast_img):
        pass
