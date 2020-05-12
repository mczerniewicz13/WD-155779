import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,30,0.1)
s=np.sin(x)
c=np.cos(x)
plt.subplot(1,2,1)
plt.plot(x,s, label='sin(x)')
plt.plot(x,c, label='cos(x)')
plt.legend()
plt.annotate('Punkcik',xy=(9.4,-1), xytext=(9.5,-1.2),arrowprops=dict(facecolor='black', shrink=0.05))


y = np.arange(1,21)
plt.subplot(1,2,2)
plt.plot(y, 1/y, 'g:>', label='Wymierna')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,len(y),0,1])
plt.annotate('Punkcik2',xy=(5,0.2), xytext=(6,0.3),arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()