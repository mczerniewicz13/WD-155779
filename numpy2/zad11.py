import numpy as np 
a = np.arange(12)
a1 = a.reshape(3,4)
a2 = a.reshape(4,3)
a3 = a.reshape(2,6)
print(a1.ravel())
print(a2.ravel())
print(a3.ravel())
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# Identyczne