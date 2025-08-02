"""class op():
    class_var=0
    def __init__(self,var):
        op.class_var +=10
        self.var=var
        print("object variable :", var)
        print("class variable",op.class_var)
        
    def __del__(self):
        op.class_var-=1
        print("obj var with %d is deleted"%self.var)

obj1=op(11)
obj2=op(12)
obj3=op(13)"""


class Numbers:
    def __init__(self, myList):
        self.myList = myList

    def __getitem__(self, index):
        return self.myList[index]

    def __setitem__(self, index, val):
        self.myList[index] = val

NumList = Numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(NumList[5])
NumList[3] = 100
print(NumList.myList)
