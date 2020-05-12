import numpy as np 
import matplotlib.pyplot as plt
x = np.arange(1,21)
plt.plot(x, 1/x, label='Wymierna')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,len(x),0,1])

plt.show()