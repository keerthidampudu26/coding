import pandas as pd 
try:
    df=pd.read_csv("hospital_data.csv")
    print("\n original hospital DataFrame")
    print(df)
#add a status column ,based on age
    df['status']=df['age'].apply(lambda x: 'senior' if x>=50 else 'adult' if x<=18 else 'unknown')
    print('\n daataframe with coloumn ')
    print(df)
#saving to csv file
    df.to_csv("hospital_data_updated.csv",index=False)
    print("\n modified dataframe saved to'hospital_data_updated.csv'")
except FileNotFoundError:
    print("The file does not exist in the specified location.")

    
    
    