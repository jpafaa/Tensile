# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:09:03 2019

@author: pfair
"""


import numpy as np
import matplotlib.pyplot as plt
from skimage import data,filters,io
from skimage.feature import canny
from skimage.exposure import equalize_adapthist
from skimage.color import rgb2gray
from skimage.transform import (rotate, hough_line, hough_line_peaks,
                               probabilistic_hough_line)
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)




x_l=0.0
plt.rcParams['font.size'] = 9
#change input to be read from script file.
image = io.imread('CsCF.jpg')
#infile=input('Input filename: ')
#image=io.imread(infile)
#convert to 8 bit greyscale
grey=rgb2gray(image)
dims=image.shape
print(dims)
# set the mask threshold level 
#this is a bit arbirary and should be changed.
#possibly use minium threhold in skimage?
vreddish = image[:, :, 0] > 150
otsu_th = threshold_otsu(image)
nib_th = threshold_niblack(image)
sa_th = threshold_sauvola(image)
binary_niblack = image > nib_th
binary_sauvola = image > sa_th
binary_otsu = image > otsu_th

vmask = image[vreddish]
fig, axes = plt.subplots(2, 3, figsize=(25, 25), sharex=True, sharey=True)
ax = axes.ravel()
ax[0].imshow(image)
ax[0].set_title('colour image')
ax[1].imshow(grey)
ax[1].set_title('greyscale')
ax[2].imshow(vreddish)
ax[2].set_title('Mask > 150')
ax[3].imshow(binary_otsu,cmap=plt.cm.gray)
ax[3].set_title('otsu')
ax[4].imshow(binary_niblack,cmap=plt.cm.gray)
ax[4].set_title('niblack')
ax[5].imshow(binary_sauvola,cmap=plt.cm.gray)
ax[5].set_title('sauvola')