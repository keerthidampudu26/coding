import re
t='my rollnumber is 328'
m=re.search(r'\d+', t)#d means one or more digits
if m:
    print('number found',m.group())
else:
    print("no match")    
#print(m.group())
