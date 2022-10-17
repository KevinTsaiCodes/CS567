import matplotlib.pyplot as plt
import ContrastStretching as CS

file = 'Stair.jpg'

if __name__ == '__main__':
    gray_img = CS.ColorModel.rgb2gray(file)
    output_IMG = CS.ContrastStretching.normalize(gray_img)

    plt.subplot(1, 2, 1)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Gray Scale')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2, 2, 2)
    plt.imshow(output_IMG, cmap='gray')
    plt.title('Contrast Stretching')
    plt.xticks([])
    plt.yticks([])

    #  Histogram Plotting of Original Image and Results
    gray_img = CS.HistogramImage.histogram(gray_img)
    output_IMG = CS.HistogramImage.histogram(output_IMG)

    plt.show()
