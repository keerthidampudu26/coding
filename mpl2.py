import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,'b-',x,y2,'r--')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('multiple lines in single plot call')
plt.legend()
plt.grid()
plt.show()
plt.pause(100)