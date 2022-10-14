import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import ContrastStretching as CS

file = 'Station.jpg'

if __name__ == '__main__':
    gray_img = CS.ColorModel.rgb2gray(file)
