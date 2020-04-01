#zad1
lista=[]
for x in range(0,100,4):
    lista+=[x]
plik = open("podz6.txt","w")
plik.writelines(str(lista))
plik.close()