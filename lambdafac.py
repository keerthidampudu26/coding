'''fa=(lambda f:lambda n: 1 if n==0 else
n*f(f)(n-1))(lambda f:lambda n: 1 
             if n==0 else n*f(f)(n-1))
print(fa(4))
l=(lambda s:s+int(m))
print(l(1234))
s=0
n=int(input())
m=str(n)
l=[ s for i in m if i>0 s=+i]
print(l)
x=lambda n:n+22
print(x(1))
a=lambda n1,n2:n1+n2
print(a(1,2))
b=lambda x,y:x if x>y else y
print(b(5,2))
n=[1,2,3,4,5,6]
e=list(filter(lambda nu:nu%2==0,n))
print(e)
n=[1,2,3,4,5,6]
e=list(map(lambda( n)))
P=[(1,2),(44,33),(66,66)]
r=sorted(P,key=lambda x:x[1])
print(r)
def b(n):
    return lambda x:x*n
a=b(2)
print(a(5))
def a(n):
    return n**3
b=lambda x:x**3
print(a(2))
print(b(3))
l=lambda a,b:a if len(a)>len(b) else b
print(l('keerthi','dampudubiyyam'))
print(l('krishna','keerthi')
da=['keerthi','krishna','kumari','kishore']
u=[(lambda x:x.upper())(d) for d in da]
print(u)
s="keerthi"
u=[(lambda x:x[::-1])(s)]
print(u)
w=['keerthi','kumari','krishna']
rw=[(lambda w1:w1[::-1])(word) for word in w]
print(rw)'''
l=['hi',' ','students','bye']
lc=[w  for w in l if  w!=" "]
print(lc)
'''l=['hi',' ','students','bye']
for i in l:
    if i !=" ":
        print(i)'''


