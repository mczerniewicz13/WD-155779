from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot( 121 , projection = '3d' )
x=np.random.rand(20)
y=np.random.rand(20)
z=x+y
ax.scatter(x,y,z,marker='o',c='red',label='z=x+y')
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )
plt.legend()

ax=fig.add_subplot(122, projection = '3d')
a=np.random.rand(5)
b=np.random.rand(5)
d=a+b
ax.plot(a,b,d, label='d=a+b')
ax.set_xlabel( 'A' )
ax.set_ylabel( 'B' )
ax.set_zlabel( 'D' )
plt.legend()
plt.show()
