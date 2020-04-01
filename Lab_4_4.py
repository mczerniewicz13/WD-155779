class NaZakupy:
    nazwa_produktu="x"
    ilosc=1
    jednostka_miary="kg"
    cena_jed=1
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    
    def wyświetl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    
    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)
    
    def ile_kosztuje(self):
        print(str(self.ilosc*self.cena_jed) + " zł/" + self.jednostka_miary)
    
    






ziemniak=NaZakupy("ziemniak",4,"kg",3)
ziemniak.wyświetl_produkt()
ziemniak.ile_produktu()
ziemniak.ile_kosztuje()
