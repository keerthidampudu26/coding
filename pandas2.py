import pandas as pd
print("enter 4 random numbers ,space seperated")
numbers=input().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!=4:
        raise ValueError("please provide exactly 4 numbers")
    td=pd.Series(numbers)
    print(td)
    filtered=td[td>10]
    print("values>10")
    print(filtered)
except ValueError as e:
    print(f"Error{e}")    
    
