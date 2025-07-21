#given attributs a,b,c,d are hi,!,students,!!!
#write a nted lambda to concatinate the abcd by converting a and c to uppeer case
#output : HI! students!!!
#print((lambda a: lambda b: lambda c,d:a[::-1]+' '+b[::-1]+' '+c[::-1]+' '+d[::-1])('hi')("hello")("students","teachers"))
'''s=["keerthi",'krishna','kumari']
print([i[::-1] for i in s])'''
s=[4,6,3,8]
n=(lambda x:lambda a:a*3 if a>x  else a*3)
a_5=n(5)
o=list(map(a_5,s))
print(o)
