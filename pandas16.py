import pandas as pd 
try:
    df=pd.read_csv("hospital_data.csv")
    series=df['bill']
    print("\n original hospital bill")
    print(series)
#user manual input
    print('enter patient_id to update')    
    patient_id = input().strip()
    print('enter new bill for {patient_id}:')
    new_cost= float(input())
#update bill series and save
    if patient_id in df['patient_id'].values:
        index=df[df['patient_id']==patient_id].index[0]
        series[index]=new_cost
        print('\n updated medical bill series')
        print(series)
#update DateFrame and save        
        df['bill']=series
        df.to_csv("hospital_data.csv",index=False)
        print('\n updated csv saved to "hospital_data.csv" ')
    else:
        print(f'Error:patient_id {patient_id} not found in hospital_data.csv')
except FileNotFoundError:
    print('Error: hospital_data.csv not found')
    
        
    
    