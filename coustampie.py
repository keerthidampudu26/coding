import matplotlib.pyplot as plt
labels=['c','c++','JAVA','Python','Datascience']
price=[400,450,600,700,300]
colors=['blue','gray','brown','magenta','green']
explode=[0,0,0,0,0.4]
def label_price(pct,all_vals):
    a=int(round(pct/100.*sum(all_vals)))
    return f'Rs.{a}'
plt.figure(figsize=(12,20))
w,t,au=plt.pie(price, labels=labels,colors=colors,explode=explode,
               autopct=lambda pct:label_price(pct,price),pctdistance=0.6,
               startangle=180,
               textprops={'fontsize':12,'fontweight':'bold','color':'darkblue'},shadow=True)
plt.title('boos prices',fontsize=16,fontweight='bold')
plt.axis('equal')
plt.legend()
plt.show()
