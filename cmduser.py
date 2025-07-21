import sys
if len(sys.argv)<2:
	print("usage :python cmduser.py n1,n2...…")
n=[int(arg) for arg in sys.argv[1:]]
t=sum(n)
print(n)
print(t)
