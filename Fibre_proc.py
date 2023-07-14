# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:17:05 2019

@author: p.fairclough@sheffield.ac.uk
"""
import numpy as np
import matplotlib.pyplot as plt
import io
from skimage import data,filters,io
jimage=io.open(CsCF.jpg)
"""
with open('CsCF.jpg', 'rb') as fimage:
    jpgdata=fimage.read()
if jpgdata.startswith(b'\xff\xd8'):
    print('This is a jpeg file' )
else:
    print('This is a random file')  
    
fimage.close()

