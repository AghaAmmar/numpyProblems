# -*- coding: utf-8 -*-
import numpy as np
array = np.array([1,2,-3,4,-5,-6])
array[array<0]=0
print(array)

"""
Following is another method by using for loop and indexing
for idx, value in enumerate(array):
    if value < 0:
        array[idx]=0
        
print(array)
"""