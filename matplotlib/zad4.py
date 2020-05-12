import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(0,30,0.1)
s=np.sin(x)
s2=np.sin(x)
plt.plot(x,-1*s, label='sin(x)')
plt.plot(x,s2+2, label='sin(x)')
plt.legend()
plt.show()