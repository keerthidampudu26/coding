import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,100)
functions=[(np.sin(x),'sin(x)','red'),(np.cos(x),'cos(x)','blue'),(x**2,'x^2','green')]
for f ,label,color in functions:
    plt.plot(x,f,label=label,color=color)
plt.xlabel('x')    
plt.ylabel('y')
plt.title('multiple ines using a loop')
plt.legend()
plt.grid()
plt.show()
