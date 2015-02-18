# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros_like, zeros
from skimage.io import imread, imshow, show
from skimage.color import hsv2rgb, rgb2hsv, rgb2gray
from matplotlib.pyplot import colorbar, figure
from skimage.filter import threshold_otsu

image = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/bulles/b02.png')
im0 = rgb2gray(image)

im = zeros_like(im0)
for i in range(int(image.shape[0])):
        for j in range(int(image.shape[1])):
            im[i,j]= (int(image[i,j,0])+int(image[i,j,1])+int(image[i,j,2]))/3

thresh = threshold_otsu(im)
binary = (im > thresh)
imshow(binary)
figure()
imshow(im)
show()