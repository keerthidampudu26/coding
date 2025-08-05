import pandas as pd 
try:
    df=pd.read_csv('hospital_data.csv')
    print("\n orginal hospitsl data frame")
    print(df)
#grouping by depatment    
    grouped=df.groupby('department')['bill'].mean()
    print('\n average medical cost')
    print(grouped)
except FileNotFoundError as e :
    print("Error:Hospital_data.csv not found")    
    