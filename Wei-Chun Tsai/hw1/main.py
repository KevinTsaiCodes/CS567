import ContrastStretching as CS

file = 'Stair.jpg'

if __name__ == '__main__':
    gray_img = CS.ColorModel.rgb2gray(file)
    output_IMG = CS.ContrastStretching.normalize(gray_img)
    CS.VersusImage.plot_image(gray_img, output_IMG)
    CS.ContrastStretching.histogram(gray_img, output_IMG)
    entropy = CS.ContrastStretching.CalculateEntropy()
    print('Entropy of Contrast Stretching Method: ', entropy)
