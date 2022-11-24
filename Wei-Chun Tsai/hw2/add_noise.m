org_img = imread('Stair.jpg');
gray_img = rgb2gray(org_img);
sp = imnoise(gray_img, 'salt & pepper', 0.1);
gn = imnoise(gray_img, 'gaussian');
imwrite(sp, 'salt-and-pepper-noise.jpg');
imwrite(gn, 'gaussian-noise.jpg');
