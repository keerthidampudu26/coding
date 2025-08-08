import numpy as np
import matplotlib.pyplot as plt
np.random.seed(5)
data=np.random.randint(1,100,50)
plt.hist(data,bins=10,color='black',edgecolor='white',linewidth=5)
plt.xlabel('values range')
plt.ylabel('equality share')
plt.title('historam')
plt.show()
