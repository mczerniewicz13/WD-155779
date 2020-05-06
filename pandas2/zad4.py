import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
irys=pd.read_csv('iris.data', delimiter=',')
x=irys['sepal length']
y=irys['petal length']
colors = np.random.rand(150)
plt.scatter(x, y, c=colors)
plt.show()
