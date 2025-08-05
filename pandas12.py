import pandas as pd 
names=pd.Series(['apple','orange','kiwi'])
df=names.to_frame(name='name')
#add new coloumn 
df['price']=[50,30,20]
print(df)