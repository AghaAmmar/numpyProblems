# -*- coding: utf-8 -*-
import numpy as np

arr=np.array([[1,2],[2,3],[5,6]],dtype=np.int16)
print (arr)
print ("Shape of array ",arr.shape)
print("Dimension of Array",arr.ndim)
for x in arr:
    print("Size of element ",x.nbytes)
    


