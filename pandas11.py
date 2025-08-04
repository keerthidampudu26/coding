import pandas as pd 
try:
    df=pd.read_csv("hospital_data.csv")
    print("\n original hospital dataframe")
    print(df)
    print("\n Missing values")
    print(df.isna())
    df_filled=df.copy()
    df_filled['name']=df_filled['name'].fillna('unknown')
    df_filled['age']=df_filled['age'].fillna('unknown')
    df_filled['bill']=df_filled['bill'].fillna(0)
    print("\n dataframe after filling by defult")
    print(df_filled)
except FileNotFoundError:
    print("error:'hospital_data.csv' not found")    
    