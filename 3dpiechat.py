import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PatchCollection
labels=['c','c++','JAVA','Python','Datascience']
price=[400,450,600,700,300]
colors=['blue','gray','brown','magenta','green']
total=sum(price)
frac=[p/total for p in price]
angles=[frac*360 for fra in frac]
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111,projection='3d')
radius=1
height=0.3
start_angle=0
for i,angle  in  enumerate(angles):
    theta=np.linespace(np.deg2rad(start_angle),np.deg2rad(start_angle+angle),30)
    x=append([0],radius*np.cos(theta))
    y=append([0],radius*np.sin(theta))
    ax.plot_triurf(x,y,height,color=colors[i],alpha=0.8)
    ax.plot_triurf(x,y,height,color=colors[i],alpha=0.8)
    for j in range(len(theta-1)):
        xs=[radius*np.cos(theta[j])]


