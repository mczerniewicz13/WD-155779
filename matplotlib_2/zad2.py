from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

m = [',','.','o','v','^','>','<','1','2','3','4','8','s','p','P','*','h','H','x','X','+','d','D']
color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
def randrange(n, vmin, vmax):
    wynik = np.random.rand(n)*(vmax-vmin)+vmin
    return wynik
fig = plt.figure()
ax = fig.gca( projection = '3d' )

for a in range(5):
    kolor=color[np.random.randint(len(color))]
    mar=m[np.random.randint(len(m))]
    x=randrange(100,0,100)
    y=randrange(100,0,150)
    z=randrange(100,0,200)
    ax.scatter(x,y,z,c=kolor,marker=mar)

plt.show()

