img = imread("404795_gray.jpg"); 
img = imnoise(img,'salt & pepper',0.1);
imshow(img);
imwrite(img,"IP_HW2.png")
