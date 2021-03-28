# -*- coding: utf-8 -*-

import numpy as np

arr = np.random.randint(5,20,size=(3,3))
add=np.add(arr,arr)
sub=np.subtract(arr,arr)
multiply=np.multiply(arr,arr)
divide=np.divide(arr,arr)
print("Addition\n",add)
print("Subtraction\n",sub)
print("Multiplacation\n",multiply)
print("Divide\n",divide)
