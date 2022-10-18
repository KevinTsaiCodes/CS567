import Filter

FILE = 'arch.png'

if __name__ == '__main__':
    image = Filter.ColorModel.rgb2gray(FILE)
    Filter.Filter.box(image)
