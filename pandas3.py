import pandas as pd
print("enter 4 random numbers ,space seperated")
strings=input().split()
print("enter substring")
substring=input().strip()
try:
    if len(strings)!=5:
        raise ValueError("please provide exactly 5 numbers")
    series=pd.Series(strings)
    print('\n original series')
    print(series)
    filtere_series=series[series.str.lower().str.contains(substring.lower(),na=False)]
    print(f"strings containing'{sustring}'(case-insensitive)")                      
    print(filtere_series if not filtere_series.empty else "no match found")
except ValueError as e:
    print(f"Error{e}")    