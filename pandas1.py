import pandas as pd
print("enter 3 three names seperated with space")
names=input().split()
print("enter 3 index labels:")
indices=input().strip().split()
try:
    if len(names)!=3 or len(indices)!=3:
        raise ValueError("please provide exact names with indices")
    series=pd.Series(data=names,index=indices)
    print("created a new series:")
    print(series)
except ValueError as e:
    print(f"Error:{e}")
        