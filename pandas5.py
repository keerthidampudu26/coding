import pandas as pd 
print("enter 5 random numbers,space seperated:")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!=5:
        raise ValueError("please enter 5 numbers only")
    series=pd.Series(numbers,index=['a','b','c','d','e'])
    print('\n original series')
    print(series)
    print('\n statistics')
    print(f'mean:{series.mean()}')
    print(f'sum:{series.sum()}')
    print(f'max:{series.max()}')
    print(f'min:{series.min()}')
    print('\n Attribute')
    print(f"index:{series.index.tolist()}")
    print(f"values:{series.values.tolist()}")
    print(f"DateType:{series.dtype}")
except ValueError as e:
    print(f'error{e}')    
    