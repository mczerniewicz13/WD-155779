class Ciagi:
    ciag=[]
    def __init__(self,ciag):
        self.ciag=ciag



    def wyswietl_dane(self):
            print(self.ciag)
    


    def pobierz_elementy(self):

        print("Podaj elementy. Gdy bedziesz chcial skonczyc wciśnij x\n")

        el=0
        i=0

        while el != "x":
            self.ciag.append(input("Podaj " + str(i+1) + " element: "))
            el=self.ciag[i]
            i+=1
        del self.ciag[i-1]
    


    def pobierz_parametry(self,a1,r,il):
        self.a1 = a1
        self.r = r
        self.il = il
    


    def policz_sume(self):
        wynik = 0
        for x in range(self.il):
            wynik+=self.a1 + x * self.r
        print(wynik)

    

    def policz_elementy(self):
        for x in range(self.il):
            print("a" + str(x+1) + "=" + str(self.a1 + x * self.r))



lista=[] 
c = Ciagi(lista)
c.pobierz_elementy()
c.wyswietl_dane()
print(lista)
c.pobierz_parametry(1,1,5)
c.policz_sume()
c.policz_elementy()


