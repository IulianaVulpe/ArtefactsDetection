from skimage.io import imread, imshow, show
from skimage.color import hsv2rgb, rgb2hsv
from matplotlib.pyplot import colorbar, figure


im = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/plis/p02.png')
im_hsv = rgb2hsv(im)
print im[1,1]/25650 #=[Red Green Blue] compris entre 0 et 1
print im_hsv[1,1]  #=[Hue Saturation Value] compris entre 0 et 1
print (im_hsv[1,1,1] - im_hsv[1,1,2])*256

im_enhanced = im.copy()
for i in range(int(im.shape[0])):
        for j in range(int(im.shape[1])):
            im_enhanced[i,j] = im[i,j]+1.5*(im_hsv[i,j,1]-im_hsv[i,j,2])*255

im_enhanced_hsv = rgb2hsv(im_enhanced)

imshow(im_enhanced_hsv[:,:,0])
colorbar()
figure()
imshow(im_enhanced_hsv[:,:,1])
colorbar()
figure()
imshow(im_enhanced_hsv[:,:,2])
colorbar()
figure()
imshow(im_enhanced_hsv[:,:,1]-im_enhanced_hsv[:,:,2])
colorbar()

"""
imshow(im_hsv[:,:,0])
colorbar()
figure()
imshow(im_hsv[:,:,1])
colorbar()
figure()
imshow(im_hsv[:,:,2])
colorbar()
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

figure()
imshow(im_enhanced)
colorbar()

show()

"""
subsampled = im[0::5,0::5]
hsvsubsampled = skimage.color.rgb2hsv(1.*subsampled)
for i in range(int(hsvsubsampled.shape[0])):
        for j in range(int(hsvsubsampled.shape[1])):
            if hsvsubsampled[i,j,0]<32 and hsvsubsampled[i,j,0]>40:
                hsvsubsampled[i,j] = (0.,0.,0.)
imshow(hsvsubsampled)
figure()
rgbsubsampled = skimage.color.hsv2rgb(hsvsubsampled)
imshow(rgbsubsampled)
"""