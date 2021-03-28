# -*- coding: utf-8 -*-
import numpy as np
#For specific integer we use randint() and for float use uniform() #
arr = np.random.uniform(10,80,size=(2,2))
print("Random array generated \n",arr)
print("Minimum value",arr.min())
print('Maximum value',arr.max())
