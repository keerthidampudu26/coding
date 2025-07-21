import sys
if len(sys.argv)!=3:
	print("usage :python sample.py b")
else:
	l=float(sys.argv[1])
	b=float(sys.argv[2])
	print(l*b)