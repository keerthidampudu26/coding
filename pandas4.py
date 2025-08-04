import pandas as pd 
import numpy as np
series=pd.Series([10,np.nan,30,np.nan,50],index=['a','b','c','d','e'])
print('\n original series:')
print(series)
print("\n missing values")
print(series.isna())
filled_series=series.fillna(0)
print(filled_series)
dropped_series=series.dropna()
print("\n series after dropping missing values")
print(dropped_series)