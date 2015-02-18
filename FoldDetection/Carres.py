from skimage.io import imread, imshow, show
from numpy import zeros_like
im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/plis/p02.png')

long = int(im.shape[0])
larg = int(im.shape[1])

im_mod = im.copy()
for i in range(long):
        for j in range(larg):
            if (i%100 == 0) or (j%100 == 0):
                im_mod[i,j,1] = 255
imshow(im_mod)
show()