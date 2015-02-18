# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


import numpy as np
from numpy import zeros_like, zeros
from skimage.io import imread, imshow, show
from skimage.color import hsv2rgb, rgb2hsv, rgb2gray
from matplotlib.pyplot import colorbar, figure


im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/plis/p06.png')

im_hsv = rgb2hsv(im)
im_enhanced = im_hsv[:,:,2]
imshow(im_enhanced)
colorbar()
figure()

long = int(im.shape[0])
larg = int(im.shape[1])


print long  #900
print larg  #1600

count = 0
ts = 30 # = tile size
tiled_im = im.copy()

for l in range(int(long/ts)):
    for k in range(int(larg/ts)):
        for i in range(ts):
            for j in range(ts):
                if im_enhanced[l*ts +i, k*ts +j] > 0.90:
                    count = count + 1


        if (count > 0.8*(ts*ts)) & ((l*ts+ts) < long) & ((k*ts +ts) < larg): # plus de 80% des pixels d une tile doivent etre noirs
                tiled_im[l*ts : l*ts+4,  k*ts : k*ts+ts, 1]=255 #+3: pour que les traits soient visibles a l ecran
                tiled_im[l*ts+ts : l*ts+ts+4 ,  k*ts : k*ts+ts, 1]=255
                tiled_im[l*ts : l*ts+ts,  k*ts : k*ts+4, 1]=255
                tiled_im[l*ts : l*ts+ts,  k*ts+ts: k*ts+ts+4, 1]=255
        count=0

imshow(tiled_im)
colorbar()
"""
imshow(im_intensity)
colorbar()
figure()
"""

"""
figure()
imshow(im_hsv[:,:,1]>0.3 )
colorbar()

figure()
imshow(im_hsv[:,:,2]<0.6 )#bons resultats avec luminance
colorbar()

figure()
imshow(im)
colorbar()

figure()
imshow(im_enhanced)
colorbar()
"""


show()
