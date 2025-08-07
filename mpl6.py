import matplotlib.pyplot as plt
s=['a','b','c','d','e']
m=[77,45,80,56,24]
color=['red','green','brown','grey','orange']
bars=plt.bar(s,m,color=color,edgecolor='black',lw=3,width=0.5,align='center',hatch='//')
for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2,height+0.5,str(height),ha='center',fontsize=10)

plt.title('performance bar chart')
plt.xlabel('stdents')
plt.ylabel('maks/100')
plt.legend()
plt.grid(ls=':',lw=0.8)
plt.gca().set_facecolor('skyblue')
plt.show()