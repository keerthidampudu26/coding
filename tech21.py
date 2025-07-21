n=int(input())
n1=str(n)
m=n1[::-1]
while int(m)>0:
    x=m%10
    print(x)
    m=m/10