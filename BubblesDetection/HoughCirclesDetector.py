import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import hough_circle
from skimage.feature import peak_local_max
from skimage import filter
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte


# Load picture and detect edges
rgb = imread('C:\Users\Iuliana\Desktop\Projet imagerie\l.vulpe\l.vulpe/bulles/b03.png')
gray= rgb2gray(rgb)
image = img_as_ubyte(gray)
edges = filter.canny(image, sigma=3, low_threshold=10, high_threshold=50)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(5, 2))

# Detect two radii
hough_radii = np.arange(75, 200, 10)
hough_res = hough_circle(edges, hough_radii)

centers = []
accums = []
radii = []

for radius, h in zip(hough_radii, hough_res):
    # For each radius, extract two circles
    num_peaks = 2
    peaks = peak_local_max(h, num_peaks=num_peaks)
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

# Draw the most prominent 5 circles
image = color.gray2rgb(image)
for idx in np.argsort(accums)[::-1][:5]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy = circle_perimeter(center_y, center_x, radius)
    image[cy, cx] = (220, 20, 20)

ax.imshow(image)
plt.show()