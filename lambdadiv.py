try :
    print((lambda a: lambda b: lambda c,d: (a-b)/(c-d))(2)(1)(5,5))
except ZeroDivisionError:
    print('divison with error !!!')  
except TypeError:
    print(" Invalid Datatype")      