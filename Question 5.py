# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 01:33:00 2021
@author: User
"""
import numpy as np
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
column2=sampleArray[:,1]
print("Average of 2nd Column is :",round(np.mean(column2),2))
