import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('High-Contrast.jpg')
blur = cv2.medianBlur(img, 5)#Tranfer to 5X5
blur = cv2.medianBlur(img, 3)#Tranfer to 3X3
blur = cv2.medianBlur(img, 3)

plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(blur), plt.title('one_pass_5X5')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(blur), plt.title('two_pass_3X3')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
