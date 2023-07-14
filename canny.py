# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:27:21 2019

@author: pfair
"""
from skimage import data, exposure, img_as_float
>>> image = img_as_float(data.camera())
>>> np.histogram(image, bins=2)
(array([107432, 154712]), array([ 0. ,  0.5,  1. ]))
>>> exposure.histogram(image, nbins=2)
(array([107432, 154712]), array([ 0.25,  0.75]))
