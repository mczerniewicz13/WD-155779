from random import randint
def fortuna(n):
    nagrody=[300,500,10000,100,"BANKRUT",200,5000,1000,2000,50]
    suma=0
    for x in range(n):
        a=randint(0,9)
        print("Wypadło: " + str(nagrody[a]))
        if nagrody[a]=="BANKRUT":
            suma=0
        else:
            suma+=nagrody[a]
    print("Wygrana = " + str(suma))

fortuna(5)

