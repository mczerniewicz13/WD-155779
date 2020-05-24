zakupy={}
a='a'
b='b'
c=0
while c==0:
    a=input("Podaj produkt: ")
    if a != "KONIEC":
        b=input("Podaj ilosc: ")
        zakupy[a]=b
    else:
        c=1

print(zakupy)