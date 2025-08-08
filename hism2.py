import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
data1=np.random.randint(1,100,50)
data2=np.random.randint(1,100,50)
data3=np.random.randint(1,100,50)

plt.hist(data1,bins=10,alpha=0.5,label='dataset1',color='blue',edgecolor='black',linewidth=5)
plt.hist(data2,bins=10,alpha=0.5,label='dataset1',color='yellow',edgecolor='brown',linewidth=3)
plt.hist(data3,bins=10,alpha=0.5,label='dataset1',color='darkgreen',edgecolor='pink',linewidth=5)
plt.xlabel('values range')
plt.ylabel('frequency')
plt.title('multiple histogram overlapping')
plt.legend()
plt.show()
