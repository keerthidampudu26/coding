import matplotlib.pyplot as plt
labels=['apple','banana','kiwi','orange']
price=[30,20,40,50]
colors=['red','yellow','green','orange']
plt.pie(price,labels=labels,colors=colors,startangle=90)
plt.title('fruits')
plt.axis('equal')
plt.show()
