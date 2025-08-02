'''input =1 2  3 4 5
output=[1,'even',3,'even',5]'''
import numpy as np
a=np.array(list(map(int,input("enter numbeer").split())),dtype=object)
a[a%2==0]='even'
print(a)
