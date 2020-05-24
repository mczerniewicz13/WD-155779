from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection = '3d')
x=np.random.rand(20)
y=np.random.rand(20)
z=np.tan(x)
ax.scatter(x,y,z,marker='o',c='red')

a=np.random.rand(5)
b=np.random.rand(5)
d=np.sin(a)
ax.plot(a,b,d,c='g')

ax.set_facecolor('black')
fig.patch.set_facecolor('black')
plt.axis('off')
ax.grid(False)

plt.show()
