n1=int(input())
n2=int(input())
op=lambda a:lambda x:(x+a)**2
ns=op(n1)
print(ns(n2))