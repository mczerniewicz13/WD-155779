import numpy as np 
def pol(mat,kierunek):
    s = mat.shape
    x = s[0]
    y = s[1]
    
    if kierunek==0 and x%2!=0:
        print("Nie moge tego zrobic")
        return -1
    if kierunek==1 and y%2!=0:
        print("Nie moge tego zrobic")
        return -1
    if kierunek==0:
        a = mat[:int(x/2)]
        b = mat[int(x/2):int(x)]
    if kierunek==1:
        a = mat[:,:int(y/2)]
        b = mat[:,int(y/2):int(y)]
    print(a)
    print(b)

mat = np.array([[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 10, 11, 12]])
print(mat)
pol(mat,1)

