import pandas as pd 
import numpy as mp
data= {
    'patient_id':['p001','p002','p003','p004','p005','p006'],
    'name':['mitti','bittu','battu','chari','neelu','meenu'],
    'age':[34,30,None,60,25,50],
    'department':['carone','cancer','neuroplogy','cardiology','cancer','ICU'],
    "admissiondate":['2025-06-25','2023-02-24','2025-08-26','2025-03-28','2025-02-30','2024-02-31'],
    'bill':[70000,30000,40000,40000,30000,30000]

}
df=pd.DataFrame(data)
df.to_csv('hospital_data.csv',index=False)
print("created data succesfully")
