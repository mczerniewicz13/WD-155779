class Robaczek:
    x = 0
    y = 0
    krok = 1

    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow * self.krok
    
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
    
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok

    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
    
    def pokaz_gdzie_jestes(self):
        print("x=" + str(self.x))
        print("y=" + str(self.y))


mrowka = Robaczek(0,0,2)
mrowka.idz_w_dol(5)
mrowka.idz_w_lewo(7)
mrowka.idz_w_gore(8)
mrowka.idz_w_prawo(3)
mrowka.pokaz_gdzie_jestes()