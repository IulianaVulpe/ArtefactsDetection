# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
from numpy import zeros_like
from skimage.filter.rank import tophat
from matplotlib.pyplot import colorbar, figure
from skimage.morphology import disk, dilation, remove_small_objects
from skimage import measure
from skimage.io import imread, imshow, show
from scipy import ndimage

image = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/bulles/b01.png')

im=image[:,:,0]
im = zeros_like(im)
for i in range(int(image.shape[0])):
        for j in range(int(image.shape[1])):
            im[i,j]= (int(image[i,j,0])+int(image[i,j,1])+int(image[i,j,2]))/3


tiled_im = image.copy()
long = int(im.shape[0])
larg = int(im.shape[1])

im_tophat = tophat(im, disk(5))
imshow(im_tophat)
colorbar()
figure()

#####
seuil = (im_tophat > 120)
imshow(seuil)
figure()

seuil = remove_small_objects(seuil, 7)
imshow(seuil)
figure()

dil = dilation(seuil, disk(8))#rank max(disk)= dilatationdu blanc min
imshow(dil)
figure()

print(dil[1,1])
fill_dil = ndimage.binary_fill_holes(dil)
imshow(fill_dil)
figure()

fill_dil = remove_small_objects(fill_dil, 10000)
imshow(fill_dil)
figure()


###
lab_dil = measure.label(dil)
regions = measure.regionprops(lab_dil, 'Area', 'FilledArea')

for props in regions:
    #Area = props['Area']
    #FArea = props['FilledArea']
    #print('Area:', Area, 'Filled Area:', FArea)
    print('Area:', props.area, 'FilledArea', props.filled_area, 'Label:', props.label)
"""

    if props.filled_area > 5000:
        if lab ==
"""
"""
###
mark = zeros_like(lab)
mark[lab == 0] = 1
mark[lab > 0] = 2

ws = watershed(dil, mark)
imshow(ws)
colorbar()
figure()
print(ws[1,1])
"""

"""
for i in range(int(dil.shape[0])):
        for j in range(int(dil.shape[1])):
            if fill_dil[i,j]!= 0:              #!= 1:
                image[i,j] = (0.,0.,0.)

imshow(image)
"""

count = 0
ts = 20 # = tile size
#tiled_im = im.copy() # je le place plus haut, quand im n'est pas encore modifiée

for l in range(int(long/ts)):
    for k in range(int(larg/ts)):
        for i in range(ts):
            for j in range(ts):
                if fill_dil[l*ts +i, k*ts +j] != 0: # ici 0 et plus 1 comme dans HSV
                    count = count + 1


        if (count > 0.01*(ts*ts)) & ((l*ts+ts) < long) & ((k*ts +ts) < larg): # plus de 1% des pixels d une tile doivent etre noirs
                tiled_im[l*ts : l*ts+4,  k*ts : k*ts+ts]=(0,180,0) #+3: pour que les traits soient visibles a l ecran
                tiled_im[l*ts+ts : l*ts+ts+4 ,  k*ts : k*ts+ts]=(0,180,0)
                tiled_im[l*ts : l*ts+ts,  k*ts : k*ts+4]=(0,180,0)
                tiled_im[l*ts : l*ts+ts,  k*ts+ts: k*ts+ts+4]=(0,180,0)
        count=0


imshow(tiled_im)
colorbar()

show()