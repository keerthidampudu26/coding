'''input=1 2 3 4 5 
output=[true,2,true,4,true]'''
import numpy as np
a=np.array(list(map(int,input("enter numbers").split())),dtype=object)
a[a%2==1]=True
print(a)