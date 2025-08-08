import numpy as np
import matplotlib.pyplot as plt
np.random.seed(20)
x=np.random.rand(50)*100
y=np.random.rand(50)*100
colors=np.random.rand(50)
sizes=np.random.randint(50,500,50)
scatter=plt.scatter(x,y,c=colors,s=sizes,cmap='hot',edgecolors='black',alpha=0.7)
plt.colorbar(scatter,label='color scale')
plt.xlabel("x")
plt.ylabel('y')
plt.title('random scatter plot')
plt.grid()
plt.show()