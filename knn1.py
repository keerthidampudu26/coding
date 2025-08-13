import numpy as np 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
#from matplotlib.colors import ListedColormap
x=np.array([[1,2],[2,3],[3,4],[4,5],[6,7]])
y=np.array([0,0,1,1,1])
new_point=np.array([[4,4]])
scaler=StandardScaler()
x_scale=scaler.fit_transform(x)
scalednewpoint=scaler.transform(new_point)
k=2
knn=KNeighborsClassifier(n_neighbors=k)
knn.fit(x_scale,y)
prediction=knn.predict(scalednewpoint)
print('predicted class:',prediction[0])
h=0.04
x_min,x_max=x_scale[:,0].min()-1,x_scale[:,0].max()+1
y_min,y_max=x_scale[:,1].min()-1,x_scale[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
z=knn.predict(np.c_[xx.ravel(),yy.ravel()])
z=z.reshape(xx.shape)
plt.figure(figsize=(8,6))
plt.contourf(xx,yy,z,alpha=1)
plt.scatter(x_scale[y==0,0],x_scale[y==0,1],c='blue',marker='o',s=100,label='training point1')
plt.scatter(x_scale[y==1,0],x_scale[y==1,1],c='darkgrey' ,marker="^",s=100,label='training point2')
plt.scatter(scalednewpoint[:,0],scalednewpoint[:,1],c='black' ,marker="s",
            s=200,label='training point3')
distances,indices=knn.kneighbors(scalednewpoint)
for idx in indices[0]:
    plt.plot([scalednewpoint[0,0],x_scale[idx,0]],
             [scalednewpoint[0,1],x_scale[idx,1]],alpha=0.9)
    plt.scatter(x_scale[idx,0],x_scale[idx,1],s=150,
                marker='X',edgecolors='c',
                alpha=0.9,label='neighbours' 
                if idx==indices[0][0] else " ")
plt.legend()
plt.grid()
plt.show()