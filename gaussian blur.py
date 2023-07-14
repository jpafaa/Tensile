# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 17:03:33 2023

@author: ch1paf
"""

import imageio.v3 as iio
import matplotlib.pyplot as plt
import skimage.filters
#matplotlib widget

image = iio.imread("C:\\Users\\ch1paf\\figure_9.png")

# display the image
fig, ax = plt.subplots()
plt.imshow(image)
sigma = 1.5

# apply Gaussian blur, creating a new image
blurred = skimage.filters.gaussian(
    image, sigma=(sigma, sigma), truncate=3.5, channel_axis=2)

# display blurred image
fig, ax = plt.subplots()
plt.imshow(blurred)

