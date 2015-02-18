# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
import matplotlib.pyplot as plt
from skimage.filter.rank import tophat, gradient
from skimage.filter import sobel
from skimage.color import rgb2gray, rgb2hsv
from scipy.ndimage import gaussian_filter
from matplotlib.pyplot import colorbar, figure
from skimage.morphology import disk, dilation, erosion
import numpy as np
import scipy
import matplotlib
import skimage
import skimage.color
from skimage import data
import skimage.io

from skimage.io import imread, imshow, show
import colorsys



im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/bulles/b02.png')
#imshow(im)
#figure()

hsv = rgb2hsv(im)
imshow(hsv[:,:,2]) #value=combien de lumiere
figure()

"""
gray = rgb2gray(im)
imshow(gray)
figure()

# lisser l'image pour supprimer les points isoles
#lisse = gaussian_filter(gray, 3)
#imshow(lisse)
#figure()
"""
im_tophat = tophat(hsv[:,:,2], disk(5))
imshow(im_tophat)
colorbar()
figure()


seuil1 = (im_tophat > 140)
imshow(seuil1)
figure()

seuil2 = (im_tophat > 190)
imshow(seuil2)
figure()

seuil = seuil1 + seuil2
imshow(seuil)
figure()

dil = dilation(seuil, disk(5))


imshow(dil)
show()

"""
im_gradient = gradient(gray, disk(3))
imshow(im_gradient)
colorbar()
figure()

im_sobel = sobel(gray)
imshow(im_sobel)
colorbar()
show()
figure()
"""
