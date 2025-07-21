import sys
print("script anme:",sys.argv[0])
print("all args",sys.argv[1:])
print("number of items :",len(sys.argv))
print("including value",sys.argv)
if len(sys.argv)>1:
      print("First arg:",sys.argv[1])
else:
      print("no arguments provided")