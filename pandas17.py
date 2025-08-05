import pandas as pd 
try:
    df=pd.read_csv('hospital_data.csv')
    series=df['department']
    print('\n original data frame')
    print(series)
    clean_series=series.str.title().str.strip()
    print('\n Name series after standardizing with (titlecase and stripped space):')
    print(clean_series)
#saving to csv
    df['department']=clean_series
    df.to_csv('hospital_data.csv', index=False)
    print("data saved to csv file ")
except FileNotFoundError:
    print(" Error: The file does not exist")
    