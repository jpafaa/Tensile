# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:17:05 2019

@author: p.fairclough@sheffield.ac.uk
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,filters,io
from skimage.feature import canny
from skimage.filters import thresholding
from skimage.color import rgb2gray
from skimage.transform import (rotate, hough_line, hough_line_peaks,
                               probabilistic_hough_line)

x_l=(0,0)
i=0
plt.rcParams['font.size'] = 9
image = io.imread('CsCF.jpg')
grey=rgb2gray(image)

dims=image.shape
print(dims)
# set the mask threshold level 
vreddish = image[:, :, 0] > 150

vmask=image[vreddish]



# Line finding near vertical edges using the Hough Transform
#then rotating the image so they are vertical
vedges = canny(vreddish,0.1)
vangles=np.arange(-(1/50),(1/50),(1/200))
vh, vtheta, vd = hough_line(vedges,vangles)
vhspace,vangle,vdist=hough_line_peaks(vh, vtheta, vd)
rot_angle=np.average(vangle)*180/np.pi
for _, vangle, vdist in zip(*hough_line_peaks(vh, vtheta, vd)):
    y0_v = (vdist) / np.sin(vangle)
    y1_v = (vdist - image.shape[1] * np.cos(vangle)) / np.sin(vangle)
    x_ll=x_l
    x_l=vdist
print(vangle)
print (rot_angle)
cropped=image[0:480,(int(x_ll)-25):(int(x_l)+25)]
rot_image=rotate(cropped,rot_angle)
rot_vreddish = rot_image[:, :, 0] > 150
rot_vmask=image[rot_vreddish]
rot_vedges = canny(rot_vreddish,0.1)

#needs better thresholding than this for fine lines
rot_hreddish = rot_image[:, :, 0] > 100
rot_hmask=image[rot_hreddish]

# Line finding horizontal lines using the Hough Transform
rot_hedges = canny(rot_hreddish,0.1)
rot_hangles=np.arange(1.4,1.7,(1/180))
rot_hh, rot_htheta, rot_hd = hough_line(rot_hedges,rot_hangles)

# Generating figure
fig, axes = plt.subplots(2, 3, figsize=(15, 15), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(rot_image)
ax[0].set_title('Input image')

ax[1].imshow(rot_vreddish)
ax[1].set_title('vertical threshold')

ax[2].imshow(rot_vedges)
ax[2].set_title('vertical canny edges')

ax[3].imshow(rot_image)
for _, rot_vangle, rot_vdist in zip(*hough_line_peaks(rot_vh,              rot_vtheta, rot_vd)):
    y0_v = (rot_vdist) / np.sin(rot_vangle)
    y1_v = (rot_vdist - image.shape[1] * np.cos(rot_vangle)) / np.sin(rot_vangle)
    ax[3].plot((0, image.shape[1]), (y0_v, y1_v), '-r')
   
for _, hangle, hdist in zip(*hough_line_peaks(hh, htheta, hd)):
    y0_h = (hdist) / np.sin(hangle)
    y1_h = (hdist - image.shape[1] * np.cos(hangle)) / np.sin(hangle)
    ax[3].plot((0, image.shape[1]), (y0_h, y1_h), '-b')    
    
ax[3].set_xlim((0, image.shape[1]))
ax[3].set_ylim((image.shape[0], 0))
ax[3].set_axis_off()
ax[3].set_title('Detected lines')

ax[4].imshow(rot_hreddish)
ax[4].set_title('horizontal threshold')

ax[5].imshow(rot_hedges)
ax[5].set_title('horizontal canny edges')


plt.tight_layout()
plt.show()




                
