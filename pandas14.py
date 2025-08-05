import pandas as pd 
try:
    df=pd.read_csv('hospital_data.csv')
    print('\n original hospital data')
    print(df)
#add discount_cost column(10% discount) 
    df['discount']=df['bill']*0.9
#sorting by bill
    sorted_df=df.sort_values('bill',ascending=True) 
    print('\n Sorted  by medical bills (descending order)')
    print(sorted_df)
except FileNotFoundError:
    print("error hoaspital_data.csv is not found") 
    
 
 
 