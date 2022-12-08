import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gaussian_square.png')
blur = cv2.medianBlur(img, 5)#Tranfer to 5X5
blur = cv2.medianBlur(img, 3)#Tranfer to 3X3
blur = cv2.medianBlur(img, 3)

plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('original noise blur image')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur, cmap='gray'), plt.title('two pass 5x5 filter')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(blur, cmap='gray'), plt.title('one pass 3x3 filter')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
