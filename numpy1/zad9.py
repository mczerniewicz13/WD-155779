import numpy as np
a=1
b=1
c=1
mat = np.zeros([5,5],dtype='int32')
for x in range(0,5,1):
    for y in range(0,5,1):

        mat[x,y] = c
        c = a + b 
        a = b 
        b = c 

print(mat)