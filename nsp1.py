import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)
x=np.random.randint(1,500,500)
y=np.random.randint(1,500,500)
plt.scatter(x,y,color='red',edgecolors='black',alpha=0.7)
plt.xlabel("x")
plt.ylabel('y')
plt.title('random scatter plot')
plt.grid()
plt.show()