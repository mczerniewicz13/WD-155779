import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
def rzucaj(ilosc,lista):
    for x in range(ilosc):
        a=np.random.randint(1,6)
        b=np.random.randint(1,6)
        c=a+b
        lista.append(c)


a =[]
il = 10000
rzucaj(il,a)
plt.hist(a, bins=50, density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid(True)
plt.show()