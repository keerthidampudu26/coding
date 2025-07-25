import re 
t=input()
n=int(input())
m=re.findall(r'\d+',t)
if len(m)>=n:
    print(f'{n} number is:',m[n-1])
else:
    print("not found")
        