from random import randint
lista1=[]
lista2=[]
lista50=[]
lista100=[]
def listy():
    for x in range(20):
        lista1.append(randint(1,100))
        lista2.append(randint(1,100))

    for y in lista1:
        if y <= 50:
            lista50.append(y)
        else:
            lista100.append(y)
    print(lista50)
    print(lista100)
listy()
