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
        maxO = np.max(gray_intensity)  # Maximum pixel value in the output image
        OutP = (InP - minI) * (((maxO - minO) / (maxI - minI)) + minO)  # Output pixel value
        cv2.imwrite('misc/High-Contrast.jpg', OutP)
        return OutP


    def histogram(org_image, result_img):
        org_hist, org_bins = np.histogram(org_image.flatten(), 256, [0, 256])
        org_cdf = org_hist.cumsum()
        org_cdf_normalized = org_cdf * float(org_hist.max()) / org_cdf.max()
        plt.subplot(1, 2, 1)
        plt.plot(org_cdf_normalized, color='b')
        plt.hist(org_image.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.title('Original')

        result_hist, result_bins = np.histogram(result_img.flatten(), 256, [0, 256])
        result_cdf = result_hist.cumsum()
        result_cdf_normalized = result_cdf * float(result_hist.max()) / result_cdf.max()
        plt.subplot(1, 2, 2)
        plt.plot(result_cdf_normalized, color='g')
        plt.hist(result_img.flatten(), 256, [0, 256], color='b')
        plt.xlim([0, 256])
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.title('Contrast Stretching')

        plt.savefig('misc/HistogramImage_Original_versus_Contrast_Stretching.pdf')

        plt.show()


    def CalculateEntropy():
        filename = os.path.join('misc/', 'High-Contrast.jpg')
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_NEAREST)
        total_pixel = image.shape[0] * image.shape[1]  # the total number of pixels (image)
        oneD_array = image.ravel()  # convert gray-scale image to 1-D array
        # print(image.shape)
        # print(oneD_array)
        # print(total_pixel)  # small n in, p_i = \frac{n_i}{n (here)}
        count_not_zero = 0  # Entropy formula fraction, N. \frac{}{here}
        for notZero in oneD_array:
            if notZero != 0:
                count_not_zero = count_not_zero + 1
        # print(count_not_zero)  # Entropy formula fraction, N. \frac{}{here}
        p_i = []
        for i in range(len(oneD_array)):
            p_i.append(round((oneD_array[i] / total_pixel), 3))
        # print(p_i)
        sum_of_molecular = 0.0
        for i in range(len(oneD_array)):
            if p_i[i] != 0:
                sum_of_molecular = sum_of_molecular + (p_i[i] * np.log2(p_i[i]))
            else:
                continue
        entropy = sum_of_molecular / count_not_zero
        return entropy

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
