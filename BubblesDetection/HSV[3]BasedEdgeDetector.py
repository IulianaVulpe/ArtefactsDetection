# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
from skimage.filter.rank import tophat
from skimage.color import rgb2hsv
from matplotlib.pyplot import colorbar, figure
from skimage.morphology import disk, dilation, label, watershed
from skimage.io import imread, imshow, show

im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/bulles/b03.png')

tiled_im = im.copy()
long = int(im.shape[0])
larg = int(im.shape[1])

hsv = rgb2hsv(im)
imshow(hsv[:,:,2]) #value=combien de lumiere
figure()

im_tophat = tophat(hsv[:,:,2], disk(5))
imshow(im_tophat)
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
figure()

count = 0
ts = 20 # = tile size
#tiled_im = im.copy() # je le place plus haut, quand im n'est pas encore modifiée

for l in range(int(long/ts)):
    for k in range(int(larg/ts)):
        for i in range(ts):
            for j in range(ts):
                if ws[l*ts +i, k*ts +j] !=1:
                    count = count + 1


        if (count > 0.70*(ts*ts)) & ((l*ts+ts) < long) & ((k*ts +ts) < larg): # plus de 80% des pixels d une tile doivent etre noirs
                tiled_im[l*ts : l*ts+4,  k*ts : k*ts+ts, 1]=255 #+3: pour que les traits soient visibles a l ecran
                tiled_im[l*ts+ts : l*ts+ts+4 ,  k*ts : k*ts+ts, 1]=255
                tiled_im[l*ts : l*ts+ts,  k*ts : k*ts+4, 1]=255
                tiled_im[l*ts : l*ts+ts,  k*ts+ts: k*ts+ts+4, 1]=255
        count=0


imshow(tiled_im)
colorbar()

show()

