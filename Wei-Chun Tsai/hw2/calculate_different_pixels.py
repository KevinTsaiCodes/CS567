import cv2

if __name__ == '__main__':
    mf3_img = cv2.imread('MF3_Lena.jpg', cv2.IMREAD_GRAYSCALE)
    mf5_img = cv2.imread('MF5_Lena.jpg', cv2.IMREAD_GRAYSCALE)
    zero_img = cv2.imread('zero_padding_sNp.png', cv2.IMREAD_GRAYSCALE)
    h, w = mf3_img.shape
    h1, w1 = mf5_img.shape
    org_h, org_w = zero_img.shape
    print('Original Image Pixels: ', org_h * org_w)
    count_not_same = 0
    for i in range(0, w):
        for j in range(0, h):
            if zero_img[i, j] != mf3_img[i, j]:
                count_not_same += 1
    print("Result of Pixels (3 x 3 Median Filter and Original Image): ", count_not_same)
    count_not_same = 0
    for i in range(0, w):
        for j in range(0, h):
            if zero_img[i, j] != mf5_img[i, j]:
                count_not_same += 1
    print("Result of Pixels (5 x 5 Median Filter and Original Image): ", count_not_same)
