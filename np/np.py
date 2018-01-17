# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:45:09 2017

@author: VX
"""

import numpy as np

a = np.array([[1,2.99,3],
              [4,5,6.367]],dtype = np.int8)
b = np.array([[9,8,7],
              [6,5,4]])
c = np.array([[1,99],
              [2,6666666666],
              [3,4]])

d = ([[1, 2],
      [3, 4]])
print (d)
print (a)
print ('np of dim :',a.ndim)
print ('shape     :',a.shape)
print ('element   :',a.size)
print ('type      :',a.dtype)

print (b)
print ('np of dim :',b.ndim)
print ('shape     :',b.shape)
print ('element   :',b.size)
print ('type      :',b.dtype)

print (c)
print ('np of dim :',c.ndim)
print ('shape     :',c.shape)
print ('element   :',c.size)
print ('type      :',c.dtype)

print (a+b)
print ('np of dim :',(a+b).ndim)
print ('shape     :',(a+b).shape)
print ('element   :',(a+b).size)
print ('type      :',(a+b).dtype)

    
