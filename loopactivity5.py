n=int(input())
'''if n%1==0:
    print("other tham 1")
if n%2==0:
    print("small is 2")'''
if(n%2==0):
    print("2 is samll")
elif(n%2!=0):
    for i in range(3,n):
        if(n%i==0):
            print(i)  
    print("samll is",i)
elif(n%1==0):
    print("other than 1")
    