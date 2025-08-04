import pandas as pd 
print("enter 4 numbers,space seperated:")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!=4:
        raise ValueError("give 4 numbers only")
    series=pd.Series(numbers,index=['a','b','c','d'])
    print('\n original series')
    print(series)
    doubled=series*2
    print('\n series after doubling series')
    print(doubled)
    added=series+100
    print('\n series after adding 100')
    print(added)
except ValueError as e:
    print(f"Error {e}")    