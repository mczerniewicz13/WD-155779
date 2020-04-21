import numpy as np 
napis1="rabek"
napis2="rower"
napis3="roser"
m1 = np.array(list(napis1))
m2 = np.array(list(napis2))
m3 = np.diag(list(napis3))
m3[:,0]=m1
m3[0:1]=m2
print(m3)
