import re
t=input()
m=list(re.finditer(r'\d+',t))
if len(m)>=2:
    print("second number found",m[1].group())
elif len(m)==1:
    print("only number found",m[0].group())
else:
    print("no match")    