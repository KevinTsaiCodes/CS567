img = imread('salt-and-pepper-noise.jpg');
padding_img = padarray(img, [1, 1]);
% disp(img);
% disp(padding_img);
clear img;
% disp(padding_img);
% imshow(padding_img);
imwrite(padding_img, 's&p-noise_zero-padding.jpg');
clear padding_img;
clc;
