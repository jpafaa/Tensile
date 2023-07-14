# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:38:30 2021

@author: pfair
"""
import csv


with open("Autumn.txt", mode="r", newline='') as csvfile:
    dataS=csv.reader(csvfile, delimiter=',')
    line_count=0
    for row in dataS:
        if line_count==0:
            print(dataS[line_count])
            line_count+=1
        else:
            print(row[1])
            line_count+=1
    
    print (dataS[1])

#outfile=open("Autumn_out1.csv", mode='w')


