'''code to extract all the odd numbers rom the user input and print 
thm in list usin array of numpy
input:1 2  4 5 6 7 8 9
output:[1,3,5,7,9]
'''
import numpy as np
a=list(map(int,input("enter numbers").split()))
a=np.array(a)
odd=a[a%2==1]
print(odd)
