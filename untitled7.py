# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:59:00 2021

@author: pfair
"""
import csv
import codecs
import re
dataS = csv.reader(codecs.open('Autumn_2.txt', 'rU', 'utf-16'))
line_count = 0
for row in dataS:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(f'XXXX{row[1]}')
        line_count += 1
print(f'Processed {line_count} lines.')

DataP=dataS.encode("ascii")
DataP=re.sub("<*>", "", DataP)

for row in DataP:
   if line_count == 0:
       print(f'Column names are {", ".join(row)}')
       line_count += 1
   else:
       print(f'ZZZZ{row[1]}')
       line_count += 1
print(f'Processed {line_count} lines.')