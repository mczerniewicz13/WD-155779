class Slowa:
    slowo1 = ""
    slowo2 = ""

    def __init__(self,slowo1,slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2

    def sprawdz_czy_palindrom(self):
        lista = list(self.slowo1.lower())
        listao = list(self.slowo1.lower())
        listao.reverse()
        for i in range(len(lista)):
            if lista[i] != listao[i]:
                return False     
        return True
    

    def sprawdz_czy_metagramy(self):
        lista1 = list(self.slowo1.lower())
        lista2 = list(self.slowo2.lower())
        licznik = 0
        if len(lista1) != len(lista2):
            return False
        
        else:
            for i in range(len(lista1)):
                if lista1[i] != lista2[i]:
                    licznik += 1
            if licznik > 1:
                return False
        return True

    def wyswietl_wyrazy(self):
        print(self.slowo1)
        print(self.slowo2)
    
        


slowo = Slowa("Dama","Rama")
print(slowo.sprawdz_czy_palindrom())
print(slowo.sprawdz_czy_metagramy())
slowo.wyswietl_wyrazy()



