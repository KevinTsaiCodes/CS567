import matplotlib.pyplot as plt
import ContrastStretching as CS
import ImageProcessing as IP

file = 'Stair.jpg'

if __name__ == '__main__':
    gray_img = CS.ColorModel.rgb2gray(file)
    output_IMG = CS.ContrastStretching.normalize(gray_img)

    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Gray Scale')

    plt.subplot(1, 2, 2)
    plt.imshow(output_IMG, cmap='gray')
    plt.title('Contrast Stretching')

    plt.show()

    median_img = output_IMG.copy()
    median_img = IP.Filter.Median(median_img)

    plt.subplot(1, 2, 1)
    plt.imshow(median_img, cmap='gray')
    plt.title('Median Filter')

    plt.subplot(1, 2, 2)
    plt.imshow(output_IMG, cmap='gray')
    plt.title('Contrast Stretching Results')

    plt.show()
