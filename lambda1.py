l2=lambda a: lambda b,c:(a+b)*c
n1=int(input())
n2=int(input())
n3=int(input())
l1=l2(n3)
v=l1(n1,n2)
print(v)