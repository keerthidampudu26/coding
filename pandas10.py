import pandas as pd 
try:
  df=pd.read_csv('hospital_data.csv')
  print("\n Hospital DataFrame:")
  print(df)
  print("\n dataframeinfo:")
  print(df.info())
  print("\n summary statistics:")
  print(df.describe())
except FileNotFoundError:
    print("Error:'hospital_data'.csv'not found.")  
     
     