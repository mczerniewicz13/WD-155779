import numpy as np 
a = np.arange(81).reshape(9,9)
print(a)
# Wymiar mozemy zmieniac tak dlugo jak kolumny * wiersze jest równe ilości elementów
a=a.reshape(1,81)
print(a)
a=a.reshape(3,27)
print(a)
a=a.reshape(27,3)
print(a)
a=a.reshape(81,1)
print(a)
