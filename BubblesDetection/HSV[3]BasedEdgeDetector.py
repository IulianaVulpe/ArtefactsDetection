# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
from skimage.filter.rank import tophat
from skimage.color import rgb2hsv
from matplotlib.pyplot import colorbar, figure
from skimage.morphology import disk, dilation, label, watershed
from skimage.io import imread, imshow, show

im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/bulles/b04.png')

hsv = rgb2hsv(im)
imshow(hsv[:,:,2]) #value=combien de lumiere
figure()

im_tophat = tophat(hsv[:,:,2], disk(5))
imshow(im_tophat)
colorbar()
figure()

seuil = (im_tophat > 140)
imshow(seuil)
figure()

dil = dilation(seuil, disk(6))#rank max(disk)= dilatationdu blanc min
imshow(dil)
figure()

marker = dil > 0
lab = label(marker,8,0)+1
imshow(lab)
figure()

ws = watershed(dil, lab)
imshow(ws)
colorbar()
figure()

for i in range(int(ws.shape[0])):
        for j in range(int(ws.shape[1])):
            if ws[i,j]!= 1:
                im[i,j] = (0.,0.,0.)

imshow(im)
show()

