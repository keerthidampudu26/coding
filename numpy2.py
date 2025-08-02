'''input=1 2 3 4 5
output=[-1,2,-1,4,-1]'''
import numpy as np
a=list(map(int,input("enter numbers").split()))
a=np.array(a)
b=a[a%2==1]=-1
print(a)
