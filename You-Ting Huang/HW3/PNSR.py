import math
import cv2
import numpy as np

img1 = cv2.imread('gaussian_square.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('square.png',cv2.IMREAD_GRAYSCALE)
def calculate_psnr(img1, img2):
    # img1 and img2 have range [0, 255]
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        print ('PNSR: ',0.000)
    else:
        psnr = 10*np.log10( (255*255)/mse)
        print('PNSR: ',round(psnr,3))

calculate_psnr(img1, img2)
