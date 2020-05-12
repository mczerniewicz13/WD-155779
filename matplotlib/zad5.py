import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
irys=pd.read_csv('iris.data', delimiter=',')
x=irys['sepal length']
y=irys['sepal width']
colo=np.random.randint(0, 50, 150)
plt.scatter(x, y, c=colo, s=np.fabs(x-y))
plt.show()

