import numpy as np
from numpy import zeros_like, zeros
from skimage.io import imread, imshow, show
from skimage.color import hsv2rgb, rgb2hsv, rgb2gray
from matplotlib.pyplot import colorbar, figure


im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/plis/p05.png')
#im = im[0::2,0::2]

#im = imread('C:\Users\Iuliana\Desktop/noir.png')

im_hsv = rgb2hsv(im)
#print im[1,1]/256 #=[Red Green Blue] compris entre 0 et 1
print im_hsv[1,1]  #=[Hue Saturation Value] compris entre 0 et 1

#print (im_hsv[1,1,1] - im_hsv[1,1,2])*256
long = int(im.shape[0])
larg = int(im.shape[1])

im_enhanced = zeros_like(im)
#print im_enhanced.dtype
#im_intensity = zeros((long, larg))
#print im_intensity.dtype
imshow((1-im_hsv[:,:,1])*255.)
colorbar()
figure()
show()
for i in range(int(im.shape[0])):
        for j in range(int(im.shape[1])):
            im_enhanced[i,j] = im[i,j].astype(np.float)/256 + 1.5*(im_hsv[i,j,1]-im_hsv[i,j,2])
            #im_enhanced[i,j]= (int(im[i,j,0])+int(im[i,j,1])+int(im[i,j,2]))/3 #RuntimeWarning: overflow encountered in ubyte_scalars
            pass
#im_enhanced = rgb2gray(im)
print im_enhanced[3,4]
#print im_enhanced[300,265]

print long  #900
print larg  #1600

count = 0
ts = 7 # = tile size
tiled_im = im.copy()

for l in range(int(long/ts)):
    for k in range(int(larg/ts)):
        for i in range(ts):
            for j in range(ts):
                if im_enhanced[l*ts +i, k*ts +j,0] < 130:
                    count = count + 1


        if (count > 0.8*(ts*ts)) & ((l*ts+ts) < long) & ((k*ts +ts) < larg): # plus de 80% des pixels d une tile doivent etre noirs
                tiled_im[l*ts : l*ts+4,  k*ts : k*ts+ts, 1]=255 #+3: pour que les traits soient visibles a l ecran
                tiled_im[l*ts+ts : l*ts+ts+4 ,  k*ts : k*ts+ts, 1]=255
                tiled_im[l*ts : l*ts+ts,  k*ts : k*ts+4, 1]=255
                tiled_im[l*ts : l*ts+ts,  k*ts+ts: k*ts+ts+4, 1]=255
        count=0

""" #si on utilise rgb2gray:
for l in range(int(long/ts)):
    for k in range(int(larg/ts)):
        for i in range(ts):
            for j in range(ts):
                if im_enhanced[l*ts +i, k*ts +j] < 0.4:
                    count = count + 1


        if (count > 0.8*(ts*ts)) & ((l*ts+ts) < long) & ((k*ts +ts) < larg): # plus de 80% des pixels d une tile doivent etre noirs
                tiled_im[l*ts : l*ts+4,  k*ts : k*ts+ts]=255 #+3: pour que les traits soient visibles a l ecran
                tiled_im[l*ts+ts : l*ts+ts+4 ,  k*ts : k*ts+ts]=255
                tiled_im[l*ts : l*ts+ts,  k*ts : k*ts+4]=255
                tiled_im[l*ts : l*ts+ts,  k*ts+ts: k*ts+ts+4]=255
        count=0
"""
imshow(im_enhanced)
colorbar()
figure()

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
