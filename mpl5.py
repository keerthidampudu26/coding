import matplotlib.pyplot as plt
s=['a','b','c','d','e']
m=[77,45,80,56,24]
color=['red','green','brown','grey','orange']
plt.bar(s,m,color=color,edgecolor='black',lw=3,width=0.5,align='center',hatch='//')
plt.title('performance bar chart')
plt.xlabel('stdents')
plt.ylabel('maks/100')
plt.legend()
plt.grid(ls=':',lw=0.8)
plt.show()