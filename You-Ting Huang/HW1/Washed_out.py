import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

img= cv2.imread('403838.jpg', cv2.IMREAD_GRAYSCALE)
img_resize = cv2.resize(img, (255,255))
img2 = img_resize.copy()
img = img_resize.copy()
img2 = img2/255 #表示正規化0-255
img2 = 0.6 * img2#可調整值,對比度拉伸
img2[img2<(50/255)] = 2 * img2[img2<(50/255)]#可調整值,minimum pixel value in the input image
img2[img2>(175/255)] = 2 * img2[img2>(175/255)]#可調整值,maximum pixel value in the input image

# normalized entropy value
print(np.cumsum(np.log(img2.ravel()))/(img2.shape[0]*img2.shape[1]))


plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Gray scale')
plt.subplot(1,2,2)
plt.imshow(img2, cmap='gray')
plt.title('contrast stretching')
plt.savefig('1116021_HW1.png')
plt.show()
