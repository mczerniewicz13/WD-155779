class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


Adam = Pracownik("Adam","Buc",3000)
Robert = Menadzer("Robert","Suski",15000)

if isinstance(Adam,Menadzer):
    print("Menadzer")
else:
    print("Pracownik")

if isinstance(Robert,Menadzer):
    print("Menadzer")
else:
    print("Pracownik")

if issubclass(Menadzer,Osoba):
    print("M sub O")

if issubclass(Pracownik,Osoba):
    print("P sub O")
