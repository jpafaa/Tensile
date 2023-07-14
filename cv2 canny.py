# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:36:43 2019

@author: pfair
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('CsCF.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,400,apertureSize = 3)

lines = cv2.HoughLines(edges,20,np.pi/180,300)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',img)

#plotting
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(4, 2.5))
ax = axes.ravel()

ax[0] = plt.subplot(221)
ax[1] = plt.subplot(222)
ax[2] = plt.subplot(223)
ax[3] = plt.subplot(224)


ax[0].imshow(img)
ax[0].set_title('img')
ax[0].axis('off')

ax[1].imshow(gray, cmap=plt.cm.gray)
ax[1].set_title('grey')
ax[1].axis('off')

ax[2].imshow(edges, cmap=plt.cm.gray)
ax[2].set_title('edges')
ax[2].axis('off')


ax[3].imshow(edges)
for line in lines:
    p0, p1 = line
    ax[2].plot((p0[0], p1[0]), (p0[1], p1[1]))
ax[3].set_xlim((0, image.shape[1]))
ax[3].set_ylim((image.shape[0], 0))
ax[3].set_title('Hough')