import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure( figsize =( 8 , 3 ))
colo = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
shad=[True,False]
for a in range(5):
    c=colo[np.random.randint(0,len(colo))]
    s=shad[np.random.randint(0,len(shad))]
    ax = fig.add_subplot( 3,2,a+1 , projection = '3d' )
    _x = np.arange( 4 )
    _y = np.arange( 5 )
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax.bar3d(x, y, bottom, width, depth, top, color =c, shade = s,)
plt.show()