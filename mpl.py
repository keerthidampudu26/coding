'''linespace(0,10,100)
np.sin()
np.cos()
sublot(1,2,1) for 1
sublots(1,2,2) for 2 or  more

'''
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
plt.plot(x,y1,label='sin(x)',color='black')
plt.plot(x,y2,label='cos(x)',color='green')
plt.plot(x,y3,label='tan(x)',color='red')
plt.xlabel('x-values')
plt.ylabel('y-values',fontsize=20,la='bold',va='bold')
plt.title("mltiple lines i a plot")
plt.legend()
plt.grid()
plt.show()