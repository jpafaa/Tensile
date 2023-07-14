# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:19:23 2021

@author: pfair
"""

import csv
with open('Autumn.txt', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(reader)