'''input=[2,3,5,6,7]
output=[False,True,False,True,False]'''
import numpy as np
a=np.array(list(map(int,input("enter numbers").split())),dtype=object)
mask=a%3==0
print(mask)