# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:41:17 2020

@author: pfair
"""

import numpy as np
import time
import datetime


f_data=open('test_data1.txt', 'a')
f_data.write("Start date and time \r\n" )
             

t_s=0.0
t_start=time.time()
t_t=np.array([t_s])


while t_s<10:
    t_s=time.time()-t_start
    t_t=np.append(t_t, t_s)
    f_d=str(t_t)+","+str(np.cos(t_s))
    f_data.write('data %d\r\n' % t_s )
    time.sleep(1)
f_data.close()      
    
  
