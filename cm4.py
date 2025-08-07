import numpy as np
import matplotlib.pyplot as plt
data=['a','b','c']
x=np.arange(len(data))
v1=[5,10,15]
v2=[8,12,10]
np.random.seed(42)
colors=plt.cm.tab10(np.random.rand(2))
fig,ax=plt.subplots(figsize=(6,4))
ax.bar(x,v1,label='dataset 1',color=colors[0],edgecolor='black',alpha=0.4)
ax.bar(x,v2,label='dataset 2',color=colors[1],edgecolor='black',alpha=0.4)
ax.set_xlabel('data')
ax.set_ylabel('values')
ax.set_title('stack bar')
ax.legend()
plt.tight_layout()
plt.show()