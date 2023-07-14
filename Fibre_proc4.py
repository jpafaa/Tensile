# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:17:05 2019

@author: p.fairclough@sheffield.ac.uk
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import data,filters,io
from skimage.feature import canny
from skimage.exposure import equalize_adapthist
#from skimage.color import rgb2gray
#from skimage.morphology import disk
from skimage.filters import gaussian
from skimage.util import invert
from skimage.transform import (rotate, hough_line, hough_line_peaks,
                              probabilistic_hough_line)
x_l=0.0
plt.rcParams['font.size'] = 9
#change input to be read from script file.
image = io.imread('CsCF.jpg')
#infile=input('Input filename: ')
#image=io.imread(infile)
#convert to 8 bit greyscale
#grey=rgb2gray(image)
dims=image.shape
print(dims)
# set the mask threshold level 
#this is a bit arbirary and should be changed.
#possibly use minium threhold in skimage?
vreddish = image[:, :, 0] > 150
vmask=image[vreddish]


# Line finding for "near vertical" edges using the Hough Transform
#then rotating the image so they are vertical
vedges = canny(vreddish,0.1)
#again a bit arbitray (canny, 0.1) and should be improved
#
vangles=np.arange(-(1/50),(1/50),(1/200))
# find the vertical edges in a small range
# angles are in radians 1/50 is about 1.15 deg

vh, vtheta, vd = hough_line(vedges,vangles)
vhspace,vangle,vdist=hough_line_peaks(vh, vtheta, vd)
rot_angle=np.average(vangle)*180/np.pi
for _, vangle, vdist in zip(*hough_line_peaks(vh, vtheta, vd)):
    y0_v = (vdist) / np.sin(vangle)
    y1_v = (vdist - image.shape[1] * np.cos(vangle)) / np.sin(vangle)
    x_ll=x_l
    x_l=vdist
print('Average vertical offset angle /degrees ',rot_angle)
#need to rotate and then crop otherwise you loose data at the corners
rot_image=rotate(image,rot_angle,center=None)
#should really find the lines again and then crop 
# but the image is bigger than required.
# so I'm not worried about it.
rot_image=rot_image[0:480,(int(x_ll+20)):(int(x_l-10))]
#remove sloping background
# steps required, create blured image then subract this from the original
neg_image=invert(rot_image)
bkg_image=gaussian(rot_image, 20)
nor_image=rot_image-bkg_image

#rotate also changes the colour range from 0 to 1
#required for equalise.
#save this image so you can check its worked.
#outfile='rot_'+infile
#io.imsave(outfile,rot_image,plugin='jpg')
#io.imsave(rot_image,'rot_CsCF.jpg'

#===removed as cretes a lot of noise======
# flattend the image to remove a lighting gradient.
ad_rot_image= equalize_adapthist(rot_image,clip_limit=0.01)
#don't set clip_limit to 0.0 this doesn't work use 0.001
#clip_limit >0.1 makes no difference.
#============================================
# try 
#ad_rot_image=equalize_hist(rot_image)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#calc 10th percentile
rot_p=np.percentile(nor_image,70)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fig, axes = plt.subplots(1, 4, figsize=(15, 15))
ax = axes.ravel()

ax[0].imshow(rot_image)
ax[0].set_title('rotated image')

ax[1].imshow(bkg_image)
ax[1].set_title('background image')

ax[2].imshow(nor_image)
ax[2].set_title('rotated image')

ax[3].imshow(neg_image)
ax[3].set_title('negative image')




# Now find the vertical edges (again!)
# and calculate the horizontal separation for the Poisson's ratio
# assuming of course that the thickness changes the same amount)
#
rot_vreddish = nor_image[:, :, 0] > rot_p
#rot_vmask=rot_image[rot_vreddish]
#threshold a
rot_vedges = canny(rot_vreddish,0.1)
rot_vangles=np.arange(-(1/50),(1/50),(1/200))
rot_vh, rot_vtheta, rot_vd = hough_line(rot_vedges,theta=rot_vangles)


#also find the horizontal lines.
#needs better thresholding than this for fine lines
rot_hreddish = rot_image[:, :, 0] > rot_p
#rot_hmask=rot_image[rot_hreddish]

# Line finding horizontal lines using the Hough Transform
rot_hedges = canny(rot_hreddish,0.1)
rot_hangles=np.arange(1.7,1.8,(1/180))
rot_hh, rot_htheta, rot_hd = hough_line(rot_hedges,theta=rot_hangles)

# Generating figure
fig, axes = plt.subplots(1, 3, figsize=(15, 15), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(rot_image)
ax[0].set_title('rotated image')

ax[1].imshow(rot_vreddish)
ax[1].set_title('vertical threshold')

ax[2].imshow(rot_vedges)
ax[2].set_title('vertical canny edges')

ax[0].imshow(rot_image)
for _, rot_vangle, rot_vdist in zip(*hough_line_peaks(rot_vh, rot_vtheta, rot_vd)):
    y0_v = (rot_vdist) / np.sin(rot_vangle)
    y1_v = (rot_vdist - rot_image.shape[1] * np.cos(rot_vangle)) / np.sin(rot_vangle)
    ax[2].plot((0, rot_image.shape[1]), (y0_v, y1_v), '-r', lw=10)
   
for _, rot_hangle, rot_hdist in zip(*hough_line_peaks(rot_hh, rot_htheta, rot_hd)):
    y0_h = (rot_hdist) / np.sin(rot_hangle)
    y1_h = (rot_hdist - rot_image.shape[1] * np.cos(rot_hangle)) / np.sin(rot_hangle)
    ax[2].plot((0, rot_image.shape[1]), (y0_h, y1_h), 'y-', lw=10)    
    
ax[2].set_xlim((0, rot_image.shape[1]))
ax[2].set_ylim((rot_image.shape[0], 0))
ax[2].set_axis_off()
ax[2].set_title('Detected lines')

#ax[4].imshow(rot_hreddish)
#ax[4].set_title('horizontal threshold')

#ax[5].imshow(rot_hedges)
#ax[5].set_title('horizontal canny edges')


plt.tight_layout()
plt.show()

#need to cehck the rot_ veriations as I got lost redoing it


                
