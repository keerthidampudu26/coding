import pandas as pd 
import numpy as np 
try:
    df=pd.read_csv('hospital_data.csv') 
    series=df['age']
    print('\n original age series')
    print(series)
#replace inavlid ages <0 or >120    with NaN
    clean_series=series.where((series>=0)& (series<=120),np.nan)
    print("\n age series after replacin invalid ages with NaN")
    print(clean_series)
    df['age']=clean_series
    df.to_csv('hospital_data.csv',index=False)
    print('\n updated csv savet to "hospital_data.csv"')
except FileNotFoundError:
    print('file not found')
    