'''X-AXIS
y-axis
z-axis'''

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colorbar as colorbar
import matplotlib.colors as mcolors
import numbers as mp
s=['keerthi','kumari','krishna','kishore']
m=[10,20,30,40]
n=mcolors.Normalize(vmin=min(m),vmax=max(m))
cmap=cm.hot
#cmap=cm.viridis
c=cmap(n(m))
fig,ax=plt.subplots()
bars=ax.bar(s,m,color=c,edgecolor='black')
sm=cm.ScalarMappable(cmap=cmap,norm=n)
sm.set_array([])
cbar=plt.colorbar(sm,ax=ax)
cbar.set_label('m')
ax.set_title('Bar char with virids')
ax.set_xlabel('students')
ax.set_ylabel('marks')
plt.tight_layout()
plt.show()

