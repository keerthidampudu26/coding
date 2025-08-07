import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
y1=[30,25,50,40]
y3=[2,4,6,7]
plt.subplot(3,1,1)
plt.plot(x,y,color='red')
plt.title("first plot")
plt.subplot(3,1,2)
plt.plot(x,y1)
plt.subplot(3,1,3)
plt.plot(x,y3)
plt.title("second plot")
plt.tight_layout()
plt.legend()
plt.show()