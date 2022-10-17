import ContrastStretching as CS

file = 'Floor.jpg'

if __name__ == '__main__':
    gray_img = CS.ColorModel.rgb2gray(file)
    output_IMG = CS.ContrastStretching.normalize(gray_img)
    CS.VersusImage.plot_image(gray_img, output_IMG)
