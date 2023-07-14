# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:14:25 2019

@author: pfair
"""

import numpy as np
import cv2

gray = cv2.imread('CsCF.jpg')
edges = cv2.Canny(gray,100,150,apertureSize = 3)
cv2.imwrite('edges-50-150.jpg',edges)
minLineLength=200
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=250)

a,b,c = lines.shape
for i in range(a):
    cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.imwrite('houghlines5.jpg',gray)