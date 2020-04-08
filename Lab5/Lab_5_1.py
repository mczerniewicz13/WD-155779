class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)


class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(self.rozmiar)
        print(self.kolor)
        print(self.dla_kogo)

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra
    
    def wyswietl_dane(self):
        print(self.rodzaj_swetra)

material1 = Material("bawelna",2,3)
koszulka = Ubrania("L","czerwony","meska")
koszulka.wyswietl_dane()
sweter1=Sweter("Gruby")
sweter1.wyswietl_dane()
