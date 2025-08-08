import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
data1=np.random.randint(1,100,50)
data2=np.random.randint(1,100,50)
data3=np.random.randint(1,100,50)
bins=10
count1,bin_edges=np.histogram(data1,bins=bins,range=(0,100))
count2,_=np.histogram(data2,bins=bins,range=(0,100))
count3,_=np.histogram(data3,bins=bins,range=(0,100))
bin_centers=0.5*(bin_edges[:-1]+bin_edges[1:])
fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111,projection='3d')
dx=dy=(bin_edges[1]-bin_edges[0])*0.5
x1=bin_centers-dx
x2=bin_centers
x3=bin_centers+dx
y1=np.zeros_like(x1)
y2=np.zeros_like(x2)*1.5
y3=np.zeros_like(x3)*3
ax.bar3d(x1,y1,np.zeros_like(count1),dx,dy,count1,color='yellow',alpha=0.8,label='dataset1',edgecolor='black',linewidth=3)
ax.bar3d(x2,y2,np.zeros_like(count2),dx,dy,count2,color='green',alpha=0.8,label='dataset2',edgecolor='black',linewidth=3)
ax.bar3d(x3,y3,np.zeros_like(count2),dx,dy,count3,color='pink',alpha=0.8,label='dataset3',edgecolor='black',linewidth=3)
ax.set_xlabel("values")
ax.set_ylabel('frequency')
ax.set_title('miltiple histograms overlapping')
ax.set_yticks([0,1.5,3])
ax.set_yticklabels(['dataset1','dataset2','dataset3'])
plt.legend()
plt.show()
