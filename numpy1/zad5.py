import numpy as np 
def przekatna(dl):
    a = np.arange(dl,0,-1)
    m = np.diag(a)
    return m
print(przekatna(8))