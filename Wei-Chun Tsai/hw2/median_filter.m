zero_pd_img = imread('s&p-noise_zero-padding.jpg');
filter_med3_salt_lena =  medfilt2(zero_pd_img, [3,3]);
filter_med3_salt_lena_result =  medfilt2(filter_med3_salt_lena, [3,3]);
% imshow(filter_med3_salt_lena);
% clear filter_med3_salt_lena;
filter_med5_salt_lena =  medfilt2(zero_pd_img, [5, 5]);
% imshow(filter_med5_salt_lena);

subplot(1, 3, 1);
imshow(zero_pd_img),
title('Salt-and-Pepper Image');
clear zero_pd_img;
subplot(1, 3, 2);
imshow(filter_med3_salt_lena_result),
title('2-pass 3x3 median filter');
clear filter_med3_salt_lena_result;
clear filter_med3_salt_lena;
subplot(1, 3, 3);
imshow(filter_med5_salt_lena),
title('1-pass 5X5 median filter');
clear filter_med5_salt_lena;
clc;
