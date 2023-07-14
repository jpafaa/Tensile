# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:44:25 2019

@author: pfair
"""

import matplotlib.pyplot as plt
from skimage import data, io
from skimage.filters import threshold_otsu
from skimage.util.dtype import dtype_range
import numpy as np



plt.rcParams['font.size'] = 7
#image = data.camera()
image = io.imread('CsCF.jpg',as_gray=True)
thresh = threshold_otsu(image)
binary = image > thresh
imax=image.max()
rthresh=imax*0.6
reddish = image > rthresh
sig_mul=4.0
sig=4.0*np.std(image)
sig_im = image > sig
#plt.imshow(reddish)

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 2.5))
ax = axes.ravel()
ax[0] = plt.subplot(2, 3, 1)
ax[1] = plt.subplot(2, 3, 2)
ax[2] = plt.subplot(2, 3, 3, sharex=ax[0], sharey=ax[0])
ax[3] = plt.subplot(2, 3, 4, sharex=ax[0], sharey=ax[0])
ax[4] = plt.subplot(2, 3, 5)

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

ax[2].imshow(binary, cmap=plt.cm.gray)
ax[2].set_title('Otsu Thresholded')
ax[2].axis('off')

ax[3].imshow(reddish, cmap=plt.cm.gray)
ax[3].set_title('0.6 max Thresholded')
ax[3].axis('off')

plt.xscale('log')
ax[4].hist(image.ravel(), bins=256)
ax[4].set_title('Histogram')
ax[4].axvline(rthresh, color='r')
ax[4].axvline(sig, color='g')

ax[5].imshow(sig_im, cmap=plt.cm.gray)
ax[5].set_title( str(sig_mul) +' sigma Thresholded')
ax[5].axis('off')


plt.tight_layout()
plt.show()