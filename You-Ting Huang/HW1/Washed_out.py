import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('403838.jpg', cv2.IMREAD_GRAYSCALE)
img_resize = cv2.resize(img, (255,255))
img2 = img_resize.copy()
img = img_resize.copy()
img2 = img2/255
img2 = 0.5 * img2
img2[img2<(50/255)] = 2 * img2[img2<(50/255)]
img2[img2>(170/255)] = 2 * img2[img2>(170/255)]

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Input image')
plt.subplot(1,2,2)
plt.imshow(img2, cmap='gray')
plt.title('Output image')
plt.savefig('result.pdf')
plt.show()
