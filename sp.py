'''scatter plot-x,y'''
import matplotlib.pyplot as plt
x=[5,6,7,3,7,5,5,5,6,7]
y=[99,86,87,88,100,86,103,87,94,78]
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("scatter plot")
plt.grid()
plt.show()