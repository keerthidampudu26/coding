m=int(input())
num=[]
c=0
c1=0
for n in range(1,m+1):
    n1=eval(input(f'enter a {n}'))
    num.append(n1)
for i in num:
    if(i>=0):
        c+=1
    else:
        c1+=1    
print(c)
print(c1)        