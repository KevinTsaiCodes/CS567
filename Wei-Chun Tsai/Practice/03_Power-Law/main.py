import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

DIR = 'images/'

if __name__ == '__main__':
    name = 'lena.png'
    file = cv2.imread(os.path.join(DIR, name), cv2.IMREAD_GRAYSCALE)
    gamma_file = file.copy()
    gamma_file = np.array((20 * (gamma_file/255)**10), dtype=np.uint8)
    plt.subplot(1, 2, 1)
    plt.title('Original')
    plt.imshow(file, cmap='gray')
    plt.subplot(1, 2, 2)
    plt.title('Gamma')
    plt.imshow(gamma_file, cmap='gray')
    plt.savefig('Power-Law (Gamma) Transformation')
    plt.show()
