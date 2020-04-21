import numpy as np 
def potega(n, k):
    a = np.logspace(1,k,num = k,base = n)
    return(a)
print(potega(2,4))