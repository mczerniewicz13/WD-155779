#zad3
tekst = ["Ala\n","ma\n","kota"]
with open("tekst.txt","w") as plik:
    plik.writelines(tekst)
with open("tekst.txt","r") as plik:
    linijki = plik.readlines()
    print(linijki)
