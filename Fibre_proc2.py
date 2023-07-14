# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:17:05 2019

@author: p.fairclough@sheffield.ac.uk
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,filters,io
from skimage.feature import canny


plt.rcParams['font.size'] = 9
image = io.imread('CsCF.jpg')
io.imshow(image)
io.show()
dims=image.shape
print(dims)
# set the mask threshold level 
reddish = image[:, :, 0] > 200
# colour the mask green
image[reddish] = [0, 255, 0]
mask=image[reddish]
#plot the image with mask data
#plt.imshow(reddish)

# Line finding using the Probabilistic Hough Transform
#image = data.camera()
#edges = canny(image, 2, 1, 20)
#edges = canny(image)

edges = canny(image)
lines = probabilistic_hough_line(edges, threshold=10, line_length=5,
                                 line_gap=3)

# Generating figure
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(image, cmap=cm.gray)
ax[0].set_title('Input image')

ax[1].imshow(edges, cmap=cm.gray)
ax[1].set_title('Canny edges')

ax[2].imshow(edges * 0)
for line in lines:
    p0, p1 = line
    ax[2].plot((p0[0], p1[0]), (p0[1], p1[1]))
ax[2].set_xlim((0, image.shape[1]))
ax[2].set_ylim((image.shape[0], 0))
ax[2].set_title('Probabilistic Hough')

for a in ax:
    a.set_axis_off()

plt.tight_layout()
plt.show()
